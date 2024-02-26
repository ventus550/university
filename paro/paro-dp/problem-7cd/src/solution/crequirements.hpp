#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class CRequirements: public BetterCandidatesValidator
{
public:
    bool validate(const Candidate& c) override
    {
    }
private:
    unsigned minCRequirements;
};
