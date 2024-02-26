#include "Candidate.hpp"
#include "CandidatesValidator.hpp"
#include <vector>
#include <memory>
#include <algorithm>

class Application
{
public:
    Application(std::vector<Candidate> c):candidates(c)
    {
    }

    void setRequirements(unsigned cpp, unsigned c, unsigned wage)
    {
        requirements = std::make_unique<CandidatesValidator>(cpp, c, wage);
    }

    std::vector<Candidate> getFilteredCandidates()
    {
        std::vector<Candidate> qualified;
        std::copy_if(candidates.begin(), candidates.end(), std::back_inserter(qualified),
                     [this](Candidate c)
                     {
                         return requirements->shouldBeHired(c);
                     });
        return qualified;
    }
private:
    std::vector<Candidate> candidates;
    std::unique_ptr<CandidatesValidator> requirements;
};
