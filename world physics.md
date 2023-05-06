
There are many beings besides humans in world of Xallaroth. Their intellect varies from that of an insect to superhuman. The players of the game are beings on the higher end of intellect, who shares with others the goal of defeating evil and saving the world.

## Soul Power

The Soul Power (`P`) determines how powerful the being is and how much impact it can have on its surroundings. It can be used for damage or healing, among many other things. It is a combination of inherent power (based on soul level and physical size) and equipment (item level).

A being has a Soul Level (`L`) between 1 and 100. It increases with experience. A being at level `L` means that this being is capable of defeating most beings of lower levels through a combination of combat strategy and abilities. A being also has a physical size (`S`) which is an integer between `-3` and `3`, with `0` being the average size of a human. A size of `-2` is the size of a rat, and a size of `2` is the size of a giant, the size of 16 humans. All playable beings have a size of `0`.

A being has equipable items, like weapons and armor. For some, usually unplayable, low intellect beings, these items grow naturally as part of their bodies, like fangs or shells. Each item has a level (`I`) between `1` and `100`. An equipped item cannot have a level that exceeds the being's soul level.

The soul power is calculated as follows: `P = 1.0964782^L * 4^S * I^1.5`

Not taking size difference into consideration, at soul level 100, the soul power is 10,000 times the soul power at soul level 1. At item level 100, the soul power is 1000 times the soul power at item level 1. The combined effect is 10,000,000 times the soul power at soul level 1 and item level 1. Size can increase the effect by a factor of 64 or decrease it by a factor of 1/64.

## Health 

All beings have health level (`H`) which, when healthy, equals `10`. When `H` reaches `0`, the being dies. It cannot exceed `10` as far as scientists have observed.

## Effects

Soul power is what feeds the fields of effect. Effects range from constructive, such as healing, growing, or building, to protective, such as shielding, defending, or absorbing, 
to destructive, such as wounding, decaying, or destroying.

When a being attacks or produces a healing effect, it is akin to creating a spatiotemporal field. The distribution of the values of the field depends on the type of attack or heal. But the integral of the field is proportional to the soul power. In the purest form, it is equal to it. 

A being health level is affected by the part of the field the being occupies. The effect is equal to the spatiotemporal integral of the field over the being spatiotemporal enclosure, divided by the being's soul power, or a variation of it depending on the realm of effect described below.

In the most basic scenario, this means that it would take `10` hits or heals to kill or fully heal a being with the same soul power as the attacker or healer. 

## Realms

There are two known realms of effect: the physical realm and the ethereal realm. The physical realm is the realm of matter. The ethereal realm is the realm of magic. The effect of an item is usually in both realms but not necessarily in the same proportion. For example, a sword is mostly physical, but will also have an ethereal effect. A wand is mostly ethereal, but it will also have a physical effect. The spatiotemporal field described above is a combination of the two effects and hence is a vector field, where the vectors are in the two dimensional realm space. To see how the this works, consider the following example: A sword with a physical-to-ethereal ratio of `2.14` will create a vector field with the unit realm vector `[0.906,0.423]`, magnified by the soul power: `F = P_attacker * [0.906,0.423]`. If an enemy is hit by this sword, the damage will depend not only the enemy's soul power (which incorporates the defensive gear items' levels) but also the gear's physical-to-ethereal ratio. The absorption is maximum if the realm vectors have the same direction and decreases as the two vectors diverge. To calculate the effect on the enemy, `P_attacker` is divided by a proportion of `P_enemy` equal to the square of the cosine of the angle between the two vectors. If, for example, the gear's realm vector is the same as the sword's, the damage will be calculated as `|F|/(P_enemy * dot(F/|F|, [0.906,0.423])^2) = P_attacker / P_enemy`. If the enemy's gear is more ethereal, the damage will be higher. In the worst case scenario, the enemy's gear is pure ethereal, with a zero physical-to-ethereal ratio (realm univ vector is `[0,1]`). The inverse of the square of the unit vectors dot product will be `1/0.423^2 = 5.6`, which will result in a damage of `5.6 * P_attacker / P_enemy`. If the sword was perfectly balanced (physical-to-ethereal ratio of `1`), the damage would be as low as `P_attacker / P_enemy` if the gear is also perfectly balanced, and as high as `2.0 * P_attacker / P_enemy` if the gear is pure physical or ethereal. If the sword was pure physical, the damage would be `P_attacker / P_enemy` if the gear is also pure physical, `2.0 * P_attacker / P_enemy` if the gear is perfectly balanced, and infinite (one-hit-kill) if the gear is pure ethereal as it would have no defense whatsoever in the physical realm (the dot product would be zero).

The physical-to-ethereal ratio of an impact (the defense impact by gear items, for example) depends on the ratio of all the items that contribute to that impact combined in a proportional way to how these items contribute to the soul power, i.e., a weighted average of their unit realm vectors, where the weight is `I^1.5`.

An item that is 100% pure is very rare. If you consider the realm vector angle, items found in nature are normally distributed around the balanced point (45 degrees). The standard deviation is 20 degrees. This means that 68% of the items found in nature have a realm vector angle between 25 and 65 degrees. There are ways of purifying items, but it is a very expensive process involving blending the item with purer items that get destroyed in the process. It can be reasoned that a pure weapon item would be desireable since the most sought after defensive gear will tend to be balanced in order to counter weapons that are unbalanced in either direction. But why would it be desireable to get a pure defensive items given that it could result in an extremely vulnerable situation? The answer lies in the Realm Crossing effect, which is described next.

## Realm Crossing

Realm Crossing is a special effect that can be found in all items with varying degrees. Realm crossing can allow an item to act in its current realm and in the opposite realm at the same time. It is akin to a quantum mechanical effect with the main difference being that the choice, instead of being probabilistic, will always be the one that maximizes the item's effect. The realm crossing effect is a value between 0% and 100%. At 0%, there is no effect. At 100%, the effect is that the item's realm vector keeps its current value, the value of its mirrored vector in the opposite realm, and every realm vector in between. For example, a sword with a physical-to-ethereal ratio of 2.14 will have a realm vector of `[0.906,0.423]` and a realm crossing effect of 100% will result in it spanning all realm vectors between that vector and the realm vector of `[0.423,0.906]`. A 50% effect will always result in extending to the balanced realm vector of `[0.707,0.707]`. It follows that the purer the item, the more it benefits from realm crossing. 

It is also important to note that if a field gets created due to an item with realm crossing, each being within the field will be affected individually by the choice that maximizes the effect of the item that created the field.

Items within such a field may themselves have a realm crossing effect, maximizing their own effect. Mathematically, the result is a [minmax](https://en.wikipedia.org/wiki/Minimax)-like choice. That is, the item creating the effect will assume the realm vector that maximizes its effect given the affected item's optimal choice (which tries to minimize the effect) of realm vector.

One can imagine the advantage of having a pure defensive gear, a pure weapon, or a pure healing item with a realm crossing effect of 100%. It is extremely rare to find an item with a realm crossing effect of more than 10%. 

## Power Prism

Soul power can be channeled into a power prism. Without it, soul power is channeled equally towards all types of effects. The power prism can alter this balance by channeling more power towards certain effects while channeling less power towards others. Beings in this world have a natural power prism that is determined by their species, but intelligent beings figured out away to alter their power prism giving them control over what effects their soul power gets channelled into. A being can for example channel more power into constructive and protective effects, away from destructive ones.

