#pragma once
#include <memory>

class Candidate;

class BetterCandidatesValidator
{
public:
    void add(std::unique_ptr<BetterCandidatesValidator> c)
    {
        if (next == nullptr)
            next->add(move(c));
        else
            next = move(c);
    }

    bool shouldBeHired(const Candidate& c)
    {
        if (next == nullptr)
        {
             return validate(c);
        }
        return validate(c) and next->shouldBeHired(c);
    }

protected:
    virtual bool validate(const Candidate& c) = 0;

private:
    std::unique_ptr<BetterCandidatesValidator> next;
};
