#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class WageRequirements: public BetterCandidatesValidator
{
public:
    bool validate(const Candidate& c) override
    {
    }
private:
    unsigned maxPreferredWage;
};
