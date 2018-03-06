{-# LANGUAGE RankNTypes #-}
module Lib (Interval, overlapsWith, insertSorted) where

type Interval a = (a, a)

overlapsWith :: (Ord a) => Interval a -> Interval a -> Bool
overlapsWith iv iv' = go iv iv' || go iv' iv
  where
    go (l,u) (l',_) = l <= l' && l' <= u

insertSorted :: (Ord a) => Interval a -> [Interval a] -> [Interval a]
insertSorted iv [] = [iv]
insertSorted iv@(l,u) ivs@(iv'@(l',u') : rest) =
  case compare u l' of
    LT -> iv : ivs
    EQ -> (l,u') : rest
    GT -> case compare l u' of
      GT -> iv' : insertSorted iv rest
      _  -> overlapUntil (l',u) ivs

overlapUntil :: (Ord a) => Interval a -> [Interval a] -> [Interval a]
overlapUntil iv@(l,u) ivs@((l',u') : rest)
  = case compare u u' of
      GT -> overlapUntil iv rest
      _  -> case compare u l' of
              LT -> iv : ivs
              _  -> (l,u') : rest
overlapUntil iv [] = [iv]
