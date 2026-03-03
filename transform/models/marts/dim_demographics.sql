with staging as (
    select 
        md5(cast(mal_id as varchar)) as anime_id,
        coalesce(demographics, 'Unspecified') as demographics_cleaned
    from {{ ref('stg_anime') }}
),

unnested_demographics as (
    select
        anime_id,
        -- This 'unnests' the list so 1 anime becomes N rows
        unnest(split(demographics_cleaned, ', ')) as demographic
    from staging
)

select * from unnested_demographics