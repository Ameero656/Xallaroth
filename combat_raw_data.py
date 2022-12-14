combat_raw_data = {
    'skills': {
        'Solar Flare': {
            'attributeType': ['light', 'magic'],
            'damage': 150,
            'cooldown': 5,
            'initiative': 90,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 4,
            'targets': 1
        },
        'Golden Shower': {
            'attributeType': ['magic', 'light'],
            'damage': 0,
            'cooldown': 3,
            'initiative': 7,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1.3,
            'selfTarget': False,
            'range': 9,
            'targets': 1
        },
        'Magic Missles': {
            'attributeType': ['magic'],
            'damage': 30,
            'cooldown': 0,
            'initiative': 30,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 8,
            'targets': 3
        },
        'Rainbow Shot': {
            'attributeType':
            ['magic', 'light', 'dark', 'fire', 'water', 'earth', 'air'],
            'damage':
            60,
            'cooldown':
            3,
            'initiative':
            48,
            'wound':
            False,
            'poison':
            False,
            'stun':
            False,
            'imobilize':
            False,
            'muddle':
            False,
            'disarm':
            False,
            'Strengthen':
            False,
            'damageRecievedMultiplier':
            1,
            'selfTarget':
            False,
            'range':
            5,
            'targets':
            1
        },
        'Sentient Torpedo': {
            'attributeType': ['magic', 'water'],
            'damage': 15,
            'cooldown': 6,
            'initiative': 32,
            'wound': False,
            'poison': False,
            'stun': True,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 9,
            'targets': 1
        },
        'Blood Thorns': {
            'attributeType': ['magic', 'light'],
            'damage': 30,
            'cooldown': 5,
            'initiative': 66,
            'wound': True,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 3,
            'targets': 3
        },
        'Golden Vow': {
            'attributeType': ['magic', 'light'],
            'damage': 0,
            'cooldown': 5,
            'initiative': 3,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': True,
            'damageRecievedMultiplier': 1,
            'selfTarget': True,
            'range': 1,
            'targets': 1
        },
        'Crystal Storm': {
            'attributeType': ['magic', 'light', 'earth', 'water'],
            'damage': 50,
            'cooldown': 6,
            'initiative': 78,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': True,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 3,
            'targets': 5
        },
        'Magnet Sphere': {
            'attributeType': ['magic', 'fire', 'earth'],
            'damage': 55,
            'cooldown': 5,
            'initiative': 90,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': True,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 3,
            'targets': 3
        },
        'Toxic Bolt': {
            'attributeType': ['magic', 'earth'],
            'damage': 30,
            'cooldown': 5,
            'initiative': 12,
            'wound': False,
            'poison': True,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 4,
            'targets': 1
        },
        'Meteor Barrage': {
            'attributeType': ['magic', 'earth', 'air'],
            'damage': 55,
            'cooldown': 7,
            'initiative': 88,
            'wound': False,
            'poison': False,
            'stun': False,
            'imobilize': False,
            'muddle': False,
            'disarm': False,
            'Strengthen': False,
            'damageRecievedMultiplier': 1,
            'selfTarget': False,
            'range': 5,
            'targets': 5
        }
    },
    'armour': {
        'setArmour': {
            'helmet': {
                "Nebula's Gaze": {
                    'attributeType': 'magic',
                    'magicDamage': (300, 450),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's Hat": {
                    'attributeType': 'magic',
                    'magicDamage': (450, 600),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 150,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 35,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                }
            },
            'chestplate': {
                "Nebula's Cloak": {
                    'attributeType': 'magic',
                    'magicDamage': (400, 650),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 3),
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's' Cloak": {
                    'attributeType': 'magic',
                    'magicDamage': (550, 700),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 150,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 3),
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 35,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                }
            },
            'gloves': {
                "Nebula's Grasp": {
                    'attributeType': 'magic',
                    'magicDamage': (350, 500),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's Grasp": {
                    'attributeType': 'magic',
                    'magicDamage': (500, 650),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 25,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 35,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                },
                "Ghost's Grasp": {
                    'attributeType': ['magic', 'air'],
                    'magicDamage': (250, 400),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'ghost',
                    'manaPointLevelRequirement': 15,
                    'physicalPointLevelRequirement': 0,
                    'focusPointLevelRequirement': 20
                },
                "Ghost's Gauntlet": {
                    'attributeType': ['magic', 'air'],
                    'magicDamage': (250, 400),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'ghost',
                    'manaPointLevelRequirement': 15,
                    'physicalPointLevelRequirement': 0,
                    'focusPointLevelRequirement': 20
                }
            },
            'pants': {
                "Nebula's Leggings": {
                    'attributeType': 'magic',
                    'magicDamage': (300, 450),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 2),
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's Leggings": {
                    'attributeType': 'magic',
                    'magicDamage': (450, 600),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 2),
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Specter's Leggings": {
                    'attributeType': 'magic',
                    'magicDamage': (200, 350),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 800,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 2),
                    'setBonusID': 'specter',
                    'manaPointLevelRequirement': 20,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 10
                }
            },
            'belt': {
                "Nebula's Belt": {
                    'attributeType': 'magic',
                    'magicDamage': (150, 300),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 100,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's Belt": {
                    'attributeType': 'magic',
                    'magicDamage': (300, 450),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 35,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                },
                "Specter's Belt": {
                    'attributeType': 'magic',
                    'magicDamage': (100, 250),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 550,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 20,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 10
                }
            },
            'boots': {
                "Nebula's Boots": {
                    'attributeType': 'magic',
                    'magicDamage': (300, 450),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'nebula',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                },
                "Sorcerer's Boots": {
                    'attributeType': 'magic',
                    'magicDamage': (450, 600),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 250,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusID': 'sorcerer',
                    'manaPointLevelRequirement': 30,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 30
                }
            },
            'rings': {
                "Ring of Might": {
                    'attributeType': 'magic',
                    'magicDamage': (400, 550),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'spirit',
                    'manaPointLevelRequirement': 15,
                    'physicalPointLevelRequirement': 10,
                    'focusPointLevelRequirement': 5
                },
                "Ring of Courage": {
                    'attributeType': 'magic',
                    'magicDamage': (50, 150),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 300,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'spirit',
                    'manaPointLevelRequirement': 10,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 15
                },
                "Ring of Darkness": {
                    'attributeType': ['magic', 'dark'],
                    'magicDamage': (200, 350),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'elementalist',
                    'manaPointLevelRequirement': 20,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                },
                "Ring of Light": {
                    'attributeType': ['magic', 'light'],
                    'magicDamage': (200, 350),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 50,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'elementalist',
                    'manaPointLevelRequirement': 20,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                }
            },
            'amulet': {
                "Amulet of Life": {
                    'attributeType':
                    ['magic', 'water', 'earth', 'fire', 'air'],
                    'magicDamage': (250, 400),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 500,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusID': 'elementalist',
                    'manaPointLevelRequirement': 20,
                    'physicalPointLevelRequirement': 5,
                    'focusPointLevelRequirement': 25
                }
            }
        }
    },
    'weapons': {
        'setWeapons': {
            'oneHanded': {
                "Inferno Rod": {
                    'attributeType': ['magic', 'fire'],
                    'weaponType': 'rod',
                    'magicDamage': 800,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusId': 'inferno',
                    'manaPointRequirement': 20,
                    'strengthPointRequirement': 5,
                    'focusPointRequirement': 10
                },
                "Inferno Staff": {
                    'attributeType': ['magic', 'fire'],
                    'weaponType': 'staff',
                    'magicDamage': 850,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusId': 'inferno',
                    'manaPointRequirement': 25,
                    'strengthPointRequirement': 6,
                    'focusPointRequirement': 15
                },
                "Orb of Flames": {
                    'attributeType': ['magic', 'fire'],
                    'weaponType': 'orb',
                    'magicDamage': 900,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': 0,
                    'setBonusId': 'shadowflame',
                    'manaPointRequirement': 30,
                    'strengthPointRequirement': 5,
                    'focusPointRequirement': 30
                },
                "Book of Shadows": {
                    'attributeType': ['magic', 'darkness'],
                    'weaponType': 'book',
                    'magicDamage': 750,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusId': 'shadowflame',
                    'manaPointRequirement': 25,
                    'strengthPointRequirement': 10,
                    'focusPointRequirement': 25
                },
                "Crystal Serpent": {
                    'attributeType': ['magic'],
                    'weaponType': 'rod',
                    'magicDamage': 550,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusId': 'Crystal',
                    'manaPointRequirement': 15,
                    'strengthPointRequirement': 5,
                    'focusPointRequirement': 5
                },
                "Crystal Scepter": {
                    'attributeType': ['magic'],
                    'weaponType': 'scepter',
                    'magicDamage': 600,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 1),
                    'setBonusId': 'Inferno',
                    'manaPointRequirement': 15,
                    'strengthPointRequirement': 5,
                    'focusPointRequirement': 5
                }
            },
            'twoHanded': {}
        },
        'legendaryWeapons': {
            'oneHanded': {},
            'twoHanded': {
                "Demon Scyth": {
                    'attributeType': ['magic', 'dark', 'fire'],
                    'weaponType': 'scyth',
                    'magicDamage': (1350, 1450),
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 2),
                    'manaPointRequirement': 25,
                    'strengthPointRequirement': 6,
                    'focusPointRequirement': 15
                },
                "Rainbow Rod": {
                    'attributeType': [
                        'magic', 'water', 'earth', 'fire', 'air', 'light',
                        'dark'
                    ],
                    'weaponType':
                    'rod',
                    'magicDamage': (850, 950),
                    'physicalDamage':
                    0,
                    'rangedDamage':
                    0,
                    'healthPointBoost':
                    0,
                    'manaPointBoost':
                    0,
                    'physicalPointBoost':
                    0,
                    'focusPointBoost':
                    0,
                    'socket': (0, 1),
                    'manaPointRequirement':
                    30,
                    'strengthPointRequirement':
                    5,
                    'focusPointRequirement':
                    15
                },
                "Nimbus Archaneum Gauntlet": {
                    'attributeType': ['magic', 'dark'],
                    'weaponType': 'gauntlet',
                    'magicDamage': 1550,
                    'physicalDamage': 0,
                    'rangedDamage': 0,
                    'healthPointBoost': 0,
                    'manaPointBoost': 0,
                    'physicalPointBoost': 0,
                    'focusPointBoost': 0,
                    'socket': (0, 5),
                    'manaPointRequirement': 40,
                    'strengthPointRequirement': 10,
                    'focusPointRequirement': 35
                }
            }
        }
    },
    'setBonusData': {
        'nebula': {
            2: 'Increases magic damage by 1500%',
            4: 'Increases light damage by 1000%',
            6: 'Increases MP value by 2000'
        },
        'sorcerer': {
            2:
            'Increase Solar Flare damage by 3000%',
            4:
            'For every set bonus item equiped, grant +100 MP value',
            6:
            'Magic damage is increased by 50% multiplied by the value of the spell cooldown'
        },
        'ghost': {
            2: 'Grants an extra weapon and ring slot'
        },
        'inferno': {
            2 : 'Boosts fire damage by 5000%'
        },
        'shadowflame': {
            2 : 'Boosts fire and dark damage by 2000%'
        },
        'crystal': {
            2 : 'All spells now deal 1200% damage add wound the enemy'
        },
        'specter': {
            2 : 'HP value is raised by 2000, rods, staffs, sceptures, and orbs deal 800% more damage'
        },
		'spirit': {
			2: 'Increases spell damage by 500%, HP value is raised by 500'
		},
		'elementalist': {
			2: 'Increase all element damage by 1500%',
			3: 'Increase MP, SP, FP by 5'
		}
		
    }
}
