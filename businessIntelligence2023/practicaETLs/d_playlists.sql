create table d_playlists
(
    sk_id            bigint PRIMARY KEY ,
    bk_id            bigint,
    name             varchar(64),
    collaborative    bool,
    last_modified_at timestamp,
    num_followers    bigint,
    num_edits        bigint
);