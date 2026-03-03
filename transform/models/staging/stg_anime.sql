with source as (
    select * from {{ source('raw_data', 'raw_anime')}}

),

renamed as (
    select
        -- some cleaning/adjustments to the table

        cast(mal_id as integer) as mal_id,

        title as title_default,
        type as media_type,
        status as airing_status,
        aired_from,
        source as anime_source,
        studios, 
        genres,
        themes,
        image_url,
        demographics,
        rating,
        synopsis,
        season,

        -- date/count fields
        coalesce(
            cast(year as integer), -- casting as integer
            cast(substring(aired_from, 1, 4) as integer) -- using the first 4 chars of the aired from (the year) to substitute, as a few are missing year
            ) as release_year,
        cast(episodes as integer) as episodes,
        
        -- numeric fields
        cast(score as numeric) as score,
        cast(scored_by as integer) as scored_by,
        cast(rank as integer) as rank,
        cast(popularity as integer) as popularity,
        cast(members as integer) as members,
        cast(favorites as integer) as favorites

    from source 

)

select * from renamed