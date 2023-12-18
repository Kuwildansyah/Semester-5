class PopularPlaylist {
    String href;
    int limit;
    String next;
    int offset;
    String previous;
    int total;
    List<PlaylistItem> items;

    PopularPlaylist({
        required this.href,
        required this.limit,
        required this.next,
        required this.offset,
        required this.previous,
        required this.total,
        required this.items,
    });

    factory PopularPlaylist.fromJson(Map<String, dynamic> json) => PopularPlaylist(
        href: json["href"],
        limit: json["limit"],
        next: json["next"],
        offset: json["offset"],
        previous: json["previous"],
        total: json["total"],
        items: List<PlaylistItem>.from(json["items"].map((x) => PlaylistItem.fromJson(x))),
    );

    Map<String, dynamic> toJson() => {
        "href": href,
        "limit": limit,
        "next": next,
        "offset": offset,
        "previous": previous,
        "total": total,
        "items": List<dynamic>.from(items.map((x) => x.toJson())),
    };
}

class PlaylistItem {
    bool collaborative;
    String description;
    ExternalUrls externalUrls;
    String href;
    String id;
    List<Image> images;
    String name;
    Owner owner;
    bool public;
    String snapshotId;
    Tracks tracks;
    String type;
    String uri;

    PlaylistItem({
        required this.collaborative,
        required this.description,
        required this.externalUrls,
        required this.href,
        required this.id,
        required this.images,
        required this.name,
        required this.owner,
        required this.public,
        required this.snapshotId,
        required this.tracks,
        required this.type,
        required this.uri,
    });

    factory PlaylistItem.fromJson(Map<String, dynamic> json) => PlaylistItem(
        collaborative: json["collaborative"],
        description: json["description"],
        externalUrls: ExternalUrls.fromJson(json["external_urls"]),
        href: json["href"],
        id: json["id"],
        images: List<Image>.from(json["images"].map((x) => Image.fromJson(x))),
        name: json["name"],
        owner: Owner.fromJson(json["owner"]),
        public: json["public"],
        snapshotId: json["snapshot_id"],
        tracks: Tracks.fromJson(json["tracks"]),
        type: json["type"],
        uri: json["uri"],
    );

    Map<String, dynamic> toJson() => {
        "collaborative": collaborative,
        "description": description,
        "external_urls": externalUrls.toJson(),
        "href": href,
        "id": id,
        "images": List<dynamic>.from(images.map((x) => x.toJson())),
        "name": name,
        "owner": owner.toJson(),
        "public": public,
        "snapshot_id": snapshotId,
        "tracks": tracks.toJson(),
        "type": type,
        "uri": uri,
    };
}

class ExternalUrls {
    String spotify;

    ExternalUrls({
        required this.spotify,
    });

    factory ExternalUrls.fromJson(Map<String, dynamic> json) => ExternalUrls(
        spotify: json["spotify"],
    );

    Map<String, dynamic> toJson() => {
        "spotify": spotify,
    };
}

class Image {
    String url;
    int height;
    int width;

    Image({
        required this.url,
        required this.height,
        required this.width,
    });

    factory Image.fromJson(Map<String, dynamic> json) => Image(
        url: json["url"],
        height: json["height"],
        width: json["width"],
    );

    Map<String, dynamic> toJson() => {
        "url": url,
        "height": height,
        "width": width,
    };
}

class Owner {
    ExternalUrls externalUrls;
    Tracks followers;
    String href;
    String id;
    String type;
    String uri;
    String displayName;

    Owner({
        required this.externalUrls,
        required this.followers,
        required this.href,
        required this.id,
        required this.type,
        required this.uri,
        required this.displayName,
    });

    factory Owner.fromJson(Map<String, dynamic> json) => Owner(
        externalUrls: ExternalUrls.fromJson(json["external_urls"]),
        followers: Tracks.fromJson(json["followers"]),
        href: json["href"],
        id: json["id"],
        type: json["type"],
        uri: json["uri"],
        displayName: json["display_name"],
    );

    Map<String, dynamic> toJson() => {
        "external_urls": externalUrls.toJson(),
        "followers": followers.toJson(),
        "href": href,
        "id": id,
        "type": type,
        "uri": uri,
        "display_name": displayName,
    };
}

class Tracks {
    String href;
    int total;

    Tracks({
        required this.href,
        required this.total,
    });

    factory Tracks.fromJson(Map<String, dynamic> json) => Tracks(
        href: json["href"],
        total: json["total"],
    );

    Map<String, dynamic> toJson() => {
        "href": href,
        "total": total,
    };
}
