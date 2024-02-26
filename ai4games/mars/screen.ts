import { Engine } from "engine"


export class CanvasScreen {

	engine   : Engine
	surface  : Array<number>
	canvas   : HTMLCanvasElement
	ctx		 : CanvasRenderingContext2D

	constructor(engine : Engine) {
		this.surface = engine.surface
		this.engine = engine
		this.canvas = document.createElement("canvas")
		document.body.appendChild(this.canvas)
		this.canvas.width = window.innerWidth
		this.canvas.height = window.innerHeight
		this.canvas.style.backgroundColor = 'black'
		this.canvas.style.position = 'absolute'
		this.ctx = this.canvas.getContext("2d")
		this.ctx.transform(1, 0, 0, -1, 0, this.canvas.height)
		this.clear()
	}
	
	polyline(coords : Array<number>, color = 'red', width = 0.5) {
		this.ctx.lineWidth = width;
		const X = [], Y = [], ctx = this.ctx,
			  scaleX = this.canvas.width / 7000,
			  scaleY = this.canvas.height / 3000 

		for (let i = 0; i < coords.length; i++)
			if (i % 2) Y.push(coords[i] * scaleY)
			else X.push(coords[i] * scaleX)
		
		ctx.strokeStyle = color;
		
		ctx.beginPath();
		for (let i = 0; i < X.length; i++) ctx.lineTo(X[i], Y[i]);
		ctx.stroke();
	}

	box(coords : [number, number], size = 1, color = 'red') {
		const
		scaleX = this.canvas.width / 7000,
		scaleY = this.canvas.height / 3000

		this.ctx.fillStyle = color
		this.ctx.fillRect(coords[0] * scaleX, coords[1] * scaleY, size * scaleX, size * scaleY)
	}

	clear(opacity = 0.5) {
		this.ctx.fillStyle = 'rgba(0,0,0,' + opacity + ')'
		this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
		this.polyline(this.surface)
	}
}
