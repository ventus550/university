enable_testing()

add_executable(
  ValidatorTests
  ValidatorTests.cpp
)
target_link_libraries(
  ValidatorTests
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(ValidatorTests)
