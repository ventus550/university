add_executable(DayOfYearTests
  day-of-year-tests.cpp)

target_link_libraries (DayOfYearTests PUBLIC DayOfYear gtest_main)
