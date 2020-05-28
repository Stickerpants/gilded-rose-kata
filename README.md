# Gilded Rose Kata

## Thoughts

* "Backstage passes" and "Conjured" currently only match one specific pass and one specific conjured item because the names are hardcoded into the update code. Should it detect _any_ pass, or _any_ conjured item?
* There's a lot of magic numbers in the code, like when things expire, the quality increases for passes / where their thresholds are. Should we pull those out into a config, maybe?
* `update_quality` will explode in complexity if we have more and more items. Would it be worth pulling out the edge cases for each item to reduce complexity?

## Gotchas

* I didn't realize at first that items "expire" when sell_in is exactly 0, because the original code wrote it to first decrement sell_in and then check `sell_in < 0`. Thankfully my tests caught that one!