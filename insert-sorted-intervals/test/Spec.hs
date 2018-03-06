import Test.HUnit
import Lib

main :: IO Counts
main = runTestTT $ TestList [TestLabel "Simple" test1
                            ,TestLabel "OverlapLower" test2
                            ,TestLabel "OverlapBoth" test3]
  where
    test1 = TestCase (assertEqual
                       "insertSorted (10,12) [(5,8),(14,20)]"
                       [(5,8),(10,12),(14,20)]
                       (insertSorted (10,12) [(5,8),(14,20)]))
    test2 = TestCase (assertEqual
                       "insertSorted (7,12) [(5,8),(14,20)]"
                       [(5,12),(14,20)]
                       (insertSorted (7,12) [(5,8),(14,20)]))
    test3 = TestCase (assertEqual
                       "insertSorted (7,15) [(5,8),(14,20)]"
                       [(5,20)]
                       (insertSorted (7,15) [(5,8),(14,20)]))
