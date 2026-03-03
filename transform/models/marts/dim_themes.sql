with staging as (
    select 
        md5(cast(mal_id as varchar)) as anime_id,
        coalesce(themes, 'Unspecified') as themes_cleaned
    from {{ ref('stg_anime') }}
),

unnested_themes as (
    select
        anime_id,
        -- This 'unnests' the list so 1 anime becomes N rows
        unnest(split(themes_cleaned, ', ')) as theme
    from staging
)

select * from unnested_themes