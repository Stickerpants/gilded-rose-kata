# Gilded Rose Kata

* Should we change how we detect certain items? "Backstage passes" and "Conjured" arguably shouldn't be hard-coded
* Should we do anything about the magic numbers?
* Should we decompose update_quality so that each item has its own function?

* Didn't realize expires "expire" _at_ zero, because it's written subtract, then check if < 0
* When Conjured items degrade, does it go 4x fast once expired? (Base doubling, expired doubling)