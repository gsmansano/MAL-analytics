with staging as (
    select * from {{ ref('stg_anime') }}
)

select

    md5(cast(mal_id as varchar)) as anime_id,
    score,
    rank,
    scored_by,
    members,
    favorites,
    popularity

from staging