select
    pokemon_types.pokemon_id,
    pokemon_name,
    pokemon_type,
    pokemon_stats.name move_name,
    total_damage
from
    /data/pokemon_types.csv pokemon_types
    join /data/pokemon.csv pokemon_stats on pokemon_types.pokemon_type = pokemon_stats.type
where
    pokemon_name = 'Squirtle'
    or (
        pokemon_name = 'Wartortle'
        and id in (31, 32)
    );
