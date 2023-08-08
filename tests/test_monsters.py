from dnd_character.monsters import Monster, SRD_monsters


def test_all_monsters_instantiation():
    """Constructs all 334 monsters from the SRD - how scary!"""
    for monster in SRD_monsters:
        assert Monster(monster).name == SRD_monsters[monster]["name"]


def test_zombie_serialization():
    zombie = Monster("zombie")
    expected_zombie = {
        "index": "zombie",
        "name": "Zombie",
        "size": "Medium",
        "type": "undead",
        "alignment": "neutral evil",
        "armor_class": [{"type": "dex", "value": 8}],
        "hit_points": 22,
        "hit_dice": "3d8",
        "hit_points_roll": "3d8+9",
        "speed": {"walk": "20 ft."},
        "strength": 13,
        "dexterity": 6,
        "constitution": 16,
        "intelligence": 3,
        "wisdom": 6,
        "charisma": 5,
        "proficiencies": [
            {
                "value": 0,
                "proficiency": {
                    "index": "saving-throw-wis",
                    "name": "Saving Throw: WIS",
                    "url": "/api/proficiencies/saving-throw-wis",
                },
            }
        ],
        "damage_vulnerabilities": [],
        "damage_resistances": [],
        "damage_immunities": ["poison"],
        "condition_immunities": [
            {"index": "poisoned", "name": "Poisoned", "url": "/api/conditions/poisoned"}
        ],
        "senses": {"darkvision": "60 ft.", "passive_perception": 8},
        "languages": "understands all languages it spoke in life but can't speak",
        "challenge_rating": 0.25,
        "xp": 50,
        "special_abilities": [
            {
                "name": "Undead Fortitude",
                "desc": "If damage reduces the zombie to 0 hit points, it must make a "
                "Constitution saving throw with a DC of 5+the damage taken, unless the "
                "damage is radiant or from a critical hit. On a success, the zombie drops "
                "to 1 hit point instead.",
            }
        ],
        "actions": [
            {
                "name": "Slam",
                "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage.",
                "attack_bonus": 3,
                "damage": [
                    {
                        "damage_type": {
                            "index": "bludgeoning",
                            "name": "Bludgeoning",
                            "url": "/api/damage-types/bludgeoning",
                        },
                        "damage_dice": "1d6+1",
                    }
                ],
                "actions": [],
            }
        ],
        "image": "/api/images/monsters/zombie.png",
        "url": "/api/monsters/zombie",
        "legendary_actions": [],
    }
    serialized_zombie = dict(zombie)
    assert all([serialized_zombie[k] == v for k, v in expected_zombie.items()])


def test_monster_function_deserializes_dict():
    roper = Monster("roper")
    assert Monster(dict(roper)) == roper
