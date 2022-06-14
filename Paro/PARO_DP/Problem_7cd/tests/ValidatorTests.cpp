#include "../src/CandidatesValidator.hpp"
#include "../src/Candidate.hpp"

#include <gtest/gtest.h>
#include <memory>
#include <climits>

namespace
{

constexpr unsigned int noMatterScore = 0;
constexpr unsigned int noMatterWage = UINT_MAX;

constexpr unsigned int worstScore = 0;
constexpr unsigned int perfectScore = 100;
constexpr unsigned int belowPerfectScore = 99;

constexpr unsigned int maxRequiredWage = 999;
constexpr unsigned int idealWage = 0;
constexpr unsigned int unacceptableWage = 1000;

constexpr bool uncooperative = false;
constexpr bool cooperative = true;

Candidate perfectCandidate{"perfectCandidate", perfectScore, perfectScore, cooperative, idealWage};
Candidate perfectButExpensive{"perfectButExpensive", perfectScore, perfectScore, cooperative, unacceptableWage};
Candidate loneWolf{"loneWolf", perfectScore, perfectScore, uncooperative, idealWage};
Candidate notPerfectInC{"notPerfectInC", perfectScore, belowPerfectScore, cooperative, idealWage};
Candidate notPerfectInCpp{"notPerfectInCpp", belowPerfectScore, perfectScore, cooperative, idealWage};
Candidate newInC{"newInC", perfectScore, worstScore, cooperative, idealWage};
Candidate newInCpp{"newInCpp", worstScore, perfectScore, cooperative, idealWage};

typedef std::unique_ptr<CandidatesValidator> SutType;

}


struct WageRequirementsTests : ::testing::Test
{
    SutType sut = std::make_unique<CandidatesValidator>(noMatterScore, noMatterScore, maxRequiredWage);
};


TEST_F(WageRequirementsTests, wageRequirementsValidatorSetToZeroShouldAcceptPerfectCandidate)
{
    ASSERT_TRUE(sut->shouldBeHired(perfectCandidate));
}

TEST_F(WageRequirementsTests, wageRequirementsValidatorShouldNotAcceptCandidateWithTooHighPreferredWage)
{
    ASSERT_FALSE(sut->shouldBeHired(perfectButExpensive));
}


struct CooperationNeededTests : ::testing::Test
{
    SutType sut = std::make_unique<CandidatesValidator>(noMatterScore, noMatterScore, noMatterWage);
};

TEST_F(CooperationNeededTests, cooperationNeededValidatorShouldAcceptPerfectCandidate)
{
    ASSERT_TRUE(sut->shouldBeHired(perfectCandidate));
}

TEST_F(CooperationNeededTests, cooperationNeededValidatorShouldNotAcceptUncooperativeCandidate)
{
    ASSERT_FALSE(sut->shouldBeHired(loneWolf));
}


struct CppRequirementsTests : ::testing::Test
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, noMatterScore, noMatterWage);
};

TEST_F(CppRequirementsTests, cppRequirementValidatorSetTo100ShouldAcceptPerfectCandidate)
{
    ASSERT_TRUE(sut->shouldBeHired(perfectCandidate));
}

TEST_F(CppRequirementsTests, cppRequirementValidatorShouldNotAcceptCandidateWithoutProperFluencyOfCpp)
{
    ASSERT_FALSE(sut->shouldBeHired(notPerfectInCpp));
}


struct CRequirementsTests : ::testing::Test
{
    SutType sut = std::make_unique<CandidatesValidator>(noMatterScore, perfectScore, noMatterWage);
};

TEST_F(CRequirementsTests, cRequirementValidatorSetTo100ShouldAcceptPerfectCandidate)
{
    ASSERT_TRUE(sut->shouldBeHired(perfectCandidate));
}

TEST_F(CRequirementsTests, cRequirementValidatorShouldNotAcceptCandidateWithoutProperFluencyOfCpp)
{
    ASSERT_FALSE(sut->shouldBeHired(notPerfectInC));
}


TEST(LoneWoflTests, setOfRequirementsWithCooperationShouldNotAcceptUncooperativeCandidate)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, perfectScore, idealWage);
    ASSERT_FALSE(sut->shouldBeHired(loneWolf));
}

TEST(CppNewbieTests, shouldAcceptCandidateNewInCppIfTheresNoSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(noMatterScore, perfectScore, idealWage);
    ASSERT_TRUE(sut->shouldBeHired(newInCpp));
}

TEST(CppNewbieTests, shouldNotAcceptCandidateNewInCppIfThereIsSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, perfectScore, idealWage);
    ASSERT_FALSE(sut->shouldBeHired(newInCpp));
}


TEST(CNewbieTests, shouldAcceptCandidateNewInCIfTheresNoSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, noMatterScore, idealWage);
    ASSERT_TRUE(sut->shouldBeHired(newInC));
}

TEST(CNewbieTests, shouldNotAcceptCandidateNewInCIfThereIsSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, perfectScore, idealWage);
    ASSERT_FALSE(sut->shouldBeHired(newInC));
}

TEST(TooHighRequestedWageTests, shouldAcceptExpensiveCandidateIfThereIsNoSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, perfectScore, noMatterWage);
    ASSERT_TRUE(sut->shouldBeHired(perfectButExpensive));
}

TEST(TooHighRequestedWageTests, shouldNotAcceptExpensiveCandidateIfThereIsSuchRequirement)
{
    SutType sut = std::make_unique<CandidatesValidator>(perfectScore, perfectScore, maxRequiredWage);
    ASSERT_FALSE(sut->shouldBeHired(perfectButExpensive));
}
