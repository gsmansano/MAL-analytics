with staging as (
    select * from {{ ref('stg_anime')}}
),

final as (
    select
        --creating our surrogate key
        md5(cast(mal_id as varchar)) as anime_id,
        --then pull the info excluding ones that repeat across animes and are going to receive deeper analysis
        mal_id,
        title_default,
        media_type,     -- could not be here and receive its own table
        airing_status,  -- same
        release_year,   -- same
        score,
        scored_by,
        rank,
        popularity,
        rating          -- same
    from staging
)

select * from final