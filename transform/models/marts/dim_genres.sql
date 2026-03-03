with staging as (
    select 
        md5(cast(mal_id as varchar)) as anime_id,
        coalesce(genres, 'Unspecified') as genres_cleaned -- just in case the genre is null, we add Unspecified for control
    from {{ ref('stg_anime') }}
),

unnested_genres as (
    select
        anime_id,
        -- This 'unnests' the list so 1 anime becomes N rows
        unnest(split(genres_cleaned, ', ')) as genre_name
    from staging
)

select * from unnested_genres