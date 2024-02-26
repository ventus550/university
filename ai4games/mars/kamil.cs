using System;
using System.Collections.Generic;
using System.Numerics;

namespace MarsArch
{
    class Genotype
    {
        public static double[,] CreateRandom(int genesAmount)
        {
            double[,] genotype = new double[genesAmount + 1, 2];

            genotype[0, 0] = 1;     //Actual index in cycle
            //genotype[0, 1] = 0;   //Actual fitness value
            for (int i = 1; i < genesAmount; i++)
            {
                double[] randomAction = Lander.getRandomAction();
                genotype[i, 0] = randomAction[0];
                genotype[i, 1] = randomAction[1];
            }
            return genotype;
        }

        public static double[,] ContinuousCrossover(double[,] genotype1, double[,] genotype2, double ratio)
        {
            int len = genotype1.GetLength(0);
            double[,] genotype = new double[len, 2];
            genotype[0, 0] = 1;
            int g1Index = (int)genotype1[0, 0];
            int g2Index = (int)genotype2[0, 0];
            for (int i = 1; i < len; i++)
            {
                genotype[i, 0] = Math.Round(ratio * genotype1[g1Index, 0] + (1 - ratio) * genotype2[g2Index, 0]);
                genotype[i, 1] = Math.Round(ratio * genotype1[g1Index, 1] + (1 - ratio) * genotype2[g2Index, 1]);
                g1Index = ++g1Index >= len ? 1 : g1Index;
                g2Index = ++g2Index >= len ? 1 : g2Index;
            }

            return genotype;
        }
        public static void PerformStep(double[,] genotype)
        {
            int actualIndex = (int)Math.Round(genotype[0, 0]);
            double[] newRandomAction = Lander.getRandomAction();
            genotype[actualIndex, 0] = newRandomAction[0];
            genotype[actualIndex, 1] = newRandomAction[1];
            genotype[0, 0] = ++actualIndex >= genotype.GetLength(0) ? 1 : actualIndex;
        }

        public static double[] GetCurrentActionToPerform(double[,] genotype)
        {
            int actualIndex = (int)genotype[0, 0];
            return new double[] { genotype[actualIndex, 0], genotype[actualIndex, 1] };
        }
    }
    class RHEAEfuncBase
    {
        public static double[][,] RandomInit(int n, int amountOfGenesInGenotype)
        {
            double[][,] population = new double[n][,];
            for (int i = 0; i < n; i++)
            {
                population[i] = Genotype.CreateRandom(amountOfGenesInGenotype);
            }
            return population;
        }

        public static double[][,] RandomMutation(double[][,] population, double threshold, int start, int amount)
        {
            for (int p = 0; p < amount; p++)
            {
                double[,] unit = population[p + start];
                int len = unit.GetLength(0);
                for (int i = 1; i < len; i++)
                {
                    if (Lander.random.NextDouble() < threshold)
                    {
                        double[] mutation = Lander.getRandomAction();
                        unit[i, 0] = mutation[0];
                        unit[i, 1] = mutation[1];
                    }
                }
            }

            return population;
        }

        public static double[][,] ContinuousCrossover(double[][,] population, int start, int count)
        {
            
            /*int amount = count / 2;
            for (int p1 = amount; p1 >= 0; p1--)
            {
                int p2 = Lander.random.Next() % amount;
                
                //population[p1 * 2 + start] = Genotype.ContinuousCrossover(population[start + p1 * 2], population[start + p2 * 2 + 1], Lander.random.NextDouble());
                //population[p1 * 2 + start + 1] = Genotype.ContinuousCrossover(population[start + p1 * 2], population[start + p2 * 2 + 1], 1 - Lander.random.NextDouble());
                
                double[,] new1 = Genotype.ContinuousCrossover(population[start + p1 * 2], population[start + p2 * 2 + 1], Lander.random.NextDouble());
                double[,] new2 = Genotype.ContinuousCrossover(population[start + p1 * 2], population[start + p2 * 2 + 1], 1 - Lander.random.NextDouble());
                population[p1 * 2 + start] = new1;
                population[p1 * 2 + start + 1] = new2;
            }
            */
            for(int p1 = start;p1<start + count; p1++)
            {
                int p2 = Lander.random.Next() % start;
                population[p1] = Genotype.ContinuousCrossover(population[p1], population[p2], 1 - Lander.random.NextDouble());
            }
            return population;
        }

        public static void Evaluate(double[][,] population, double[] state, Func<double[], double> fitness)
        {
            foreach (double[,] genotype in population)
            {
                double[] newState = Lander.Copy(state);
                int gIndex = (int)genotype[0, 0];
                int len = genotype.GetLength(0);
                do
                {
                    double[] action = new double[] { genotype[gIndex, 0], genotype[gIndex, 1] };
                    gIndex = ++gIndex >= len ? 1 : gIndex;
                    Lander.Apply(newState, action);
                }
                while (Lander.getLandingResult(newState) == 0);
                genotype[0, 1] = fitness(newState);
            }

            Array.Sort(population, (a, b) => a[0, 1].CompareTo(b[0, 1]));
        }
        public static double fitness1(double[] state)
        {

            //speed
            double speedVertical = Math.Abs(state[3]);
            speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
            double speedHorizontal = Math.Abs(state[2]);
            speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
            //angle
            double angle = state[5];
            angle *= angle;
            //dist
            double dist = Math.Pow(Lander.safeX - state[0], 2) + Math.Pow(Lander.safeY - state[1], 2);
            
            double val = (dist + 3000 * angle + 500000 * (speedHorizontal + speedVertical)) * (Math.Abs(Lander.getLandingResult(state) - 1));;
            if(Lander.getLandingResult(state)==-1)
                val += 1000*1000;

            return val;
        }

        public static double fitness2(double[] state)
        {

            //speed
            double speedVertical = Math.Abs(state[3]);
            speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
            double speedHorizontal = Math.Abs(state[2]);
            speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
            //angle
            double landerAngle = state[5];
            landerAngle *= landerAngle;
            //dist
            double
                posX = state[0],
                posY = state[1];
            double dist = Math.Pow(Lander.safeX - posX, 2) + Math.Pow(Lander.safeY - posY, 2);
            double angleToLand = Math.Atan2(Lander.safeX - posX, Lander.safeY - posY) * 180 / Math.PI;
            angleToLand *= angleToLand;
            //return Math.Abs(angleToLand) + landerAngle;
            return (dist + angleToLand + 30000 * landerAngle + 3000000 * (speedHorizontal + speedVertical)) * (Math.Abs(Lander.getLandingResult(state) - 1));
            // return (dist/10000 + 3000 * landerAngle + 100000 * (speedHorizontal + speedVertical)) *100* (Math.Abs(Lander.getLandingResult(state) - 1));
        }
        public static double fitness3(double[] state)
        {
            double
                speedVertical = Math.Abs(state[3]),
                speedHorizontal = Math.Abs(state[2]),
                landerAngle = state[5],
                posX = state[0],
                posY = state[1];

            speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
            speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
            landerAngle *= landerAngle;

            double dist = Math.Pow(Lander.safeX - posX, 2) + Math.Pow(Lander.safeY - posY, 2);
            double angleToLand = Math.Atan2(Lander.safeX - posX, Lander.safeY - posY) * 180 / Math.PI;
            angleToLand *= angleToLand;

            int res = Lander.getLandingResult(state);
            if (res == 1)
                return 0;
            else if (res == 0)
                return 1;
            //return Math.Sqrt(dist) + Math.Pow(speedHorizontal + speedVertical + landerAngle,1.5);
            else
                return 1000 * (dist + angleToLand + Math.Pow(landerAngle, 2) + Math.Pow(speedHorizontal, 2) + Math.Pow(speedVertical, 2));
        }

        public static double fitness4(double[] state)
        {

            //speed
            double speedVertical = Math.Abs(state[3]);
            speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
            double speedHorizontal = Math.Abs(state[2]);
            speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
            //angle
            double angle = state[5];
            angle *= angle;
            //dist
            double dist = Math.Pow(Lander.safeX - state[0], 2) + Math.Pow(Lander.safeY - state[1], 2);

            return (dist + 3000 * angle + 3000 * Math.Pow(speedHorizontal + speedVertical, 2)) * (Math.Abs(Lander.getLandingResult(state) - 1));
        }
         public static double fitness5(double[] state)
        {
            double speedVertical = Math.Abs(state[3]);
            speedVertical = speedVertical - 40 > 0 ? speedVertical - 40 : 0;
            double speedHorizontal = Math.Abs(state[2]);
            speedHorizontal = speedHorizontal - 20 > 0 ? speedHorizontal - 20 : 0;
            //angle
            double angle = state[5];
            angle *= angle;

            double X = state[0];
            double Y = state[1];
            double dist = 10000005;
            if (X >= 0 && X < 7000 && Y >= 0 && Y < 3000)
                dist = Lander.mapDist[(int)(X) / Lander.mapRecSize, (int)(Y) / Lander.mapRecSize];
            int mult = Math.Abs(Lander.getLandingResult(state) - 1);
            mult = mult == 0 ? 0 : 1;
            return (dist * dist + (speedHorizontal + speedVertical) * 10000 + angle * 3000) * mult;
        }
        public static double[][,] pureAndFixedExplorationUnits(double[][,] population, double[] state, double amount)
        {
            int fixedAmount = (int)Math.Round(amount / 2.0);
            double[][,] pureExploration = RandomInit((int)(Math.Round(amount)), population[0].GetLength(0) - 1);
            
            int rotation = (int)Math.Round(state[5]);
            int newRotation = (int)(Math.Atan2(state[2], state[3]) * 180 / Math.PI + 90);
            for (int i = 0; i < fixedAmount; i++)
            {
                int len = (int)(population[0].GetLength(0) - 1 + Lander.random.NextDouble() * population[0].GetLength(0)) / 2;
                int offset = newRotation - rotation;
                double[,] genotyp = pureExploration[0];
                int index = (int)Math.Round(genotyp[0, 0]);
                while (len >= 0)
                {
                    int dan = offset;
                    dan = dan > 15 ? 15 : dan;
                    dan = dan < -15 ? -15 : dan;
                    if (offset != 0)
                    {
                        genotyp[index, 0] = dan;
                    }
                    genotyp[index, 1] = 1;
                    offset -= dan;

                    len--;
                    index = ++index >= population[0].GetLength(0) ? 1 : index;
                }
            }

            /*
            for (int i = 0;  i < amount/2; i++)
            {
                int len = population[0].GetLength(0)-1;
                for (int gen = 1; gen <= len; gen++)
                {
                    pureExploration[i][gen, 1] = 4;
                   // pureExploration[i][gen, 0] = 0;
                }
            }
            */
            return pureExploration;
        }
    }
    class RHEA
    {

        public double[][,] population = new double[populationCount][,];
        public double[] state;
        public RHEA(double[] state)
        {
            this.state = state;
            this.population = this.initPopulation();
            this.evaluate(this.population, this.state);
        }

        public void Run()
        {
            var timeE = DateTime.Now.AddMilliseconds(90);
            while (DateTime.Now < timeE)
            {
                double[][,] parentSurviors = this.parentSurvivors(this.population);
                double[][,] children = this.mutation(this.crossover(this.parentSelection(this.population)));
                this.population = this.link(parentSurviors, children, this.pureExplorationUnits(this.population, this.state));
                this.evaluate(this.population, this.state);
            }
        }

        public double[] GetBestAndApply()
        {
            double[] action = Genotype.GetCurrentActionToPerform(this.population[0]);
            this.PerformStepInPopulation();
            Lander.Apply(this.state, action);
            return action;
        }

        void PerformStepInPopulation()
        {
            foreach (double[,] unit in this.population)
                Genotype.PerformStep(unit);
        }
        const int genotypeLen = 30;
        const int populationCount = 200;

        const int aPS = (int)(populationCount * 0.3);
        const int aCh = (int)(populationCount * 0.4);
        const int aE = populationCount - aPS - aCh;


        Func<double[][,], double[][,]> parentSurvivors =
            (x) => x;
        Func<double[][,], double[][,]> parentSelection =
            (x) => x;

        Func<double[][,], double[][,]> crossover =
            (x) => RHEAEfuncBase.ContinuousCrossover(x, aPS, aCh);
        Func<double[][,], double[][,]> mutation =
            (x) => RHEAEfuncBase.RandomMutation(x, 0.08, aPS, aCh);
        Func<double[][,], double[], double[][,]> pureExplorationUnits =
            (x, y) => RHEAEfuncBase.pureAndFixedExplorationUnits(x, y, aE);

        Func<double[][,]> initPopulation =
            () => RHEAEfuncBase.RandomInit(populationCount, genotypeLen);
        Func<double[][,], double[][,], double[][,], double[][,]> link =
            (x, y, z) =>
            {
                for (int s = 0, e = populationCount - 1; s < aE; s++, e--)
                    x[e] = z[s];
                return x;
            };
        Action<double[][,], double[]> evaluate = (x, y) => RHEAEfuncBase.Evaluate(x, y, RHEAEfuncBase.fitness5);
    }
    class Lander
    {
        public static Random random = null;
        const int squareSize = 500;
        public static List<int[]>[] Colisions = new List<int[]>[7000 / squareSize + 1];
        public static int[] __lastColisonPoint = null;
        public static double[] Sin;
        public static double[] Cos;

        public static double safeX;
        public static double safeY;

public static int[,] mapDist;
        public static int mapRecSize = 10;
        public static List<int[]> actualMap;
        public static void setMapDist()
        {
            int
                xL = 7000 / mapRecSize,
                yL = 3000 / mapRecSize,
                emptyValue = 1000000;
            mapDist = new int[xL, yL];
            for (int x = 0; x < xL; x++)
                for (int y = 0; y < yL; y++)
                    mapDist[x, y] = emptyValue * 5;


            //mapDist[(int)(Lander.safeX) / mapRecSize, (int)(Lander.safeY) / mapRecSize + 1] = 0;
            Queue<int[]> q = new Queue<int[]>();
            q.Enqueue(new int[] { (int)(Lander.safeX) / mapRecSize, (int)(Lander.safeY) / mapRecSize + 1, 0 });

            while (q.Count > 0)
            {
                int[] pos = q.Dequeue();
                int
                    x = pos[0],
                    y = pos[1],
                    val = pos[2];
                if (x < 0 || x >= xL || y < 0 || y >= yL || mapDist[x, y] != emptyValue * 5)
                    continue;
                bool good = true;
                int[] prevC=null;
                foreach (int[] v in actualMap)
                {
                    if (prevC != null)
                    {
                        int
                            realX = x * mapRecSize,
                            realY = y * mapRecSize;
                        if (
                              Lander.intersect(realX, realY, realX + mapRecSize, realY + mapRecSize, prevC[0], prevC[1], (int)v[0], (int)v[1]) ||
                              Lander.intersect(realX, realY + mapRecSize, realX + mapRecSize, realY, (int)prevC[0], (int)prevC[1], (int)v[0], (int)v[1]) ||

                              Lander.intersect(realX, realY, realX, realY + mapRecSize, (int)prevC[0], (int)prevC[1], (int)v[0], (int)v[1]) ||
                              Lander.intersect(realX, realY, realX + mapRecSize, realY, (int)prevC[0], (int)prevC[1], (int)v[0], (int)v[1]) ||
                              Lander.intersect(realX + mapRecSize, realY + mapRecSize, realX, realY + mapRecSize, (int)prevC[0], (int)prevC[1], (int)v[0], (int)v[1]) ||
                              Lander.intersect(realX + mapRecSize, realY + mapRecSize, realX + mapRecSize, realY, (int)prevC[0], (int)prevC[1], (int)v[0], (int)v[1])
                              )
                        {
                            mapDist[x, y] = 1 + val;
                            good = false;
                            break;
                        }
                    }
                    prevC = v;
                }
                if (good)
                    mapDist[x, y] = val;
                else
                    continue;

                for (int i = -1; i <= 1; i++)
                    for (int z = -1; z <= 1; z++)
                        if ((i == 0 || z == 0) && !(i == 0 && z == 0))
                            q.Enqueue(new int[] { x + i, y + z, val + mapRecSize });
            }
        }

        public static void ClearColisions()
        {
            Colisions = new List<int[]>[7000 / squareSize + 1];
            __lastColisonPoint = null;
        }

        public static void CalculateTrigonometry()
        {
            Lander.Sin = new double[181];
            Lander.Cos = new double[181];
            for (int i = 0; i <= 180; i++)
            {
                Lander.Sin[i] = Math.Sin(-(i - 90) * Math.PI / 180.0);
                Lander.Cos[i] = Math.Cos(-(i - 90) * Math.PI / 180.0);
            }
        }
        public static void addPointToColisions(int[] currentPoint)
        {
          
           if (actualMap == null)
                actualMap = new List<int[]>();
            actualMap.Add(currentPoint);
            if (__lastColisonPoint == null)
            {
                __lastColisonPoint = currentPoint;
                Colisions[currentPoint[0] / squareSize] = new List<int[]>();
                Colisions[currentPoint[0] / squareSize].Add(currentPoint);
                return;
            }

            int prevX = __lastColisonPoint[0];
            int prevY = __lastColisonPoint[1];
            int currX = currentPoint[0];
            int currY = currentPoint[1];
            if (currX < prevX)
            {
                currX = __lastColisonPoint[0];
                currY = __lastColisonPoint[1];
                prevX = currentPoint[0];
                prevY = currentPoint[1];
            }
            int index = prevX / squareSize;

            if (prevY == currY)
            {
                Lander.safeX = (prevX + currX) / 2.0;
                Lander.safeY = prevY;
            }

            Colisions[index].Add(currentPoint);
            index++;
            while (index * squareSize <= currX)
            {
                if (Colisions[index] == null)
                    Colisions[index] = new List<int[]>();
                Colisions[index].Add(__lastColisonPoint);
                Colisions[index].Add(currentPoint);
                index++;
            }

            __lastColisonPoint = currentPoint;
        }


        public static double[] CreateState(double X, double Y, double hSpeed, double vSpeed, double fuel, double rotation, double power)
        {
            return new double[] {
                X,//0
                Y,//1
                hSpeed,//2
                vSpeed,//3
                fuel,//4
                rotation,//5
                power,//6,
                0//7 landing result
            };
        }

        public static double[] Copy(double[] state) => (double[])state.Clone();

        public static int getLandingResult(double[] state) => (int)Math.Round(state[7]);
        public static double getRotation(double[] state) => state[5];
        public static double getPower(double[] state) => state[6];

        public static void Apply(double[] state, double[] action)
        {
            double
                 rotate = Math.Round(state[5] + action[0]),
                 power = Math.Round(state[6] + action[1]),
                 fuel = state[4],
                 landingResult = state[7];

            rotate = rotate < -90.0 ? -90.0 : rotate;
            rotate = rotate > 90.0 ? 90.0 : rotate;

            power = power < 0.0 ? 0.0 : power;
            power = power > 4.0 ? 4.0 : power;
            power = power > fuel ? fuel : power;

            fuel -= power;
            /*
            double arcAngle = -(this.controlersState.X + 0.0) * Math.PI / 180.0;
            Vector acc = new Vector(
                Math.Sin(arcAngle) * this.controlersState.Y,
                Math.Cos(arcAngle) * this.controlersState.Y + this.gravity);
             * */
            double
                //arcAngle = -(rotate) * Math.PI / 180.0,
                accX = Lander.Sin[(int)rotate + 90] * power,
                accY = Lander.Cos[(int)rotate + 90] * power - 3.711,
                //accX = Math.Sin(arcAngle) *power,
                //accY = Math.Cos(arcAngle) * power - 3.711,
                velocityX = state[2] + accX,
                velocityY = state[3] + accY,
                posX = state[0] + velocityX - accX / 2.0,
                posY = state[1] + velocityY - accY / 2.0;

            if (0.0 > posX || posX > 7000.0 ||
               0.0 > posY || posY > 3000.0 ||
               -500.0 > velocityX || velocityX > 500.0 ||
               -500.0 > velocityY || velocityY > 500.0)
                landingResult = -1;
            else
            {

                int prevX = (int)Math.Floor(state[0]);
                int currX = (int)Math.Ceiling(posX);
                if (currX < prevX)
                {
                    prevX = (int)Math.Floor(posX);
                    currX = (int)Math.Ceiling(state[0]);
                }
                int index = prevX / squareSize;
                while (index * squareSize <= currX)
                {
                    List<int[]> collisionsPoints = Lander.Colisions[index];
                    if (collisionsPoints != null)
                    {
                        int[] prevPoint = null;
                        foreach (int[] currentPoint in collisionsPoints)
                        {
                            if (prevPoint != null)
                            {
                                if (intersect(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1], posX, posY, state[0], state[1]))
                                {
                                    if (prevPoint[1] == currentPoint[1] && Math.Abs(velocityX) < 20 && Math.Abs(velocityY) <= 40 && Math.Round(rotate) == 0)
                                    {
                                        landingResult = 1;
                                        index = currX;
                                        break;
                                    }
                                    else
                                    {
                                        landingResult = -1;
                                        index = currX;
                                        break;
                                    }
                                }
                            }
                            prevPoint = currentPoint;
                        }
                    }
                    index++;
                }
            }
            state[0] = posX;
            state[1] = posY;
            state[2] = velocityX;
            state[3] = velocityY;
            state[4] = fuel;
            state[5] = rotate;
            state[6] = power;
            state[7] = landingResult;
        }

        public static double[] getRandomAction()
        {
            double rotation = (Lander.random.Next() % 31) - 15;
            double power = (Lander.random.Next() % 3) - 1;
            return new double[] { rotation, power };
        }
        //https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
        public static bool ccw(double Ax, double Ay, double Bx, double By, double Cx, double Cy)
        {
            return (Cy - Ay) * (Bx - Ax) > (By - Ay) * (Cx - Ax);
        }
        public static bool intersect(double Ax, double Ay, double Bx, double By, double Cx, double Cy, double Dx, double Dy)
        {
            return ccw(Ax, Ay, Cx, Cy, Dx, Dy) != ccw(Bx, By, Cx, Cy, Dx, Dy) && ccw(Ax, Ay, Bx, By, Cx, Cy) != ccw(Ax, Ay, Bx, By, Dx, Dy);
        }
    }

    class Program
    {

        static void Main(string[] args)
        {
            string[] inputs;
            int N = int.Parse(Console.ReadLine()); // the number of points used to draw the surface of Mars.
            Lander.random = new Random();
            for (int i = 0; i < N; i++)
            {
                inputs = Console.ReadLine().Split(' ');
                int landX = int.Parse(inputs[0]); // X coordinate of a surface point. (0 to 6999)
                int landY = int.Parse(inputs[1]); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.  
                Lander.addPointToColisions(new int[] { landX, landY });
                Console.Error.WriteLine(landX + " " + landY);
            }
            Lander.CalculateTrigonometry();
            Lander.setMapDist();

            bool isFirst = true;
            RHEA rhea = null;
            while (true)
            {
                inputs = Console.ReadLine().Split(' ');
                double X = double.Parse(inputs[0]);
                double Y = double.Parse(inputs[1]);
                double HS = double.Parse(inputs[2]); // the horizontal speed (in m/s), can be negative.
                double VS = double.Parse(inputs[3]); // the vertical speed (in m/s), can be negative.
                double F = double.Parse(inputs[4]); // the quantity of remaining fuel in liters.
                double R = double.Parse(inputs[5]); // the rotation angle in degrees (-90 to 90).
                double P = double.Parse(inputs[6]); // the thrust power (0 to 4).

                if (isFirst)
                {
                    rhea = new RHEA(Lander.CreateState(X, Y, HS, VS, F, R, P));
                    isFirst = false;
                }

                Console.Error.WriteLine("Otrzymane stan: \t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", X, Y, HS, VS, F, R, P);
                Console.Error.WriteLine("Symulowany stan: \t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", rhea.state[0], rhea.state[1], rhea.state[2], rhea.state[3],
                    rhea.state[4], rhea.state[5], rhea.state[6]);
                if (
                    X != Math.Round(rhea.state[0]) ||
                    Y != Math.Round(rhea.state[1]) ||
                    HS != Math.Round(rhea.state[2]) ||
                    VS != Math.Round(rhea.state[3]) ||
                    F != Math.Round(rhea.state[4]) ||
                    R != Math.Round(rhea.state[5]) ||
                    P != Math.Round(rhea.state[6]))
                {
                    Console.Error.WriteLine("Wrong simulation" +
                        (X != Math.Round(rhea.state[0])) +
                        (Y != Math.Round(rhea.state[1])) +
                        (HS != Math.Round(rhea.state[2])) +
                        (VS != Math.Round(rhea.state[3])) +
                        (F != Math.Round(rhea.state[4])) +
                        (R != Math.Round(rhea.state[5])) +
                        (P != Math.Round(rhea.state[6])));
                    return;
                }
                rhea.Run();
                double[] act = rhea.GetBestAndApply();
                Console.Error.WriteLine(act[0] + " " + act[1]);
                int r = (int)rhea.state[5];
                int p = (int)rhea.state[6];
                Console.WriteLine(r + " " + p);
            }
        }
    }
}