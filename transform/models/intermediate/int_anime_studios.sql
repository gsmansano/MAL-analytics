with staging as (
    select 
        md5(cast(mal_id as varchar)) as anime_id,
        coalesce(studios, 'Unspecified') as studios_cleaned --unlikely but just in case studios is empty in the table
    from {{ ref('stg_anime') }}
),

unnested_studios as (
    select
        anime_id,
        -- This 'unnests' the list so 1 anime becomes N rows
        unnest(split(studios_cleaned, ', ')) as studio
    from staging
)

select * from unnested_studios