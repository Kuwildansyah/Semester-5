import 'dart:convert';

class PopularPlaylist {
  String href;
  List<PlaylistItem> items;
  int limit;
  String next;
  int offset;
  dynamic previous;
  int total;

  PopularPlaylist({
    required this.href,
    required this.items,
    required this.limit,
    required this.next,
    required this.offset,
    required this.previous,
    required this.total,
  });

  factory PopularPlaylist.fromRawJson(String str) =>
      PopularPlaylist.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory PopularPlaylist.fromJson(Map<String, dynamic> json) =>
      PopularPlaylist(
        href: json["href"],
        items: List<PlaylistItem>.from(
            json["items"].map((x) => PlaylistItem.fromJson(x))),
        limit: json["limit"],
        next: json["next"],
        offset: json["offset"],
        previous: json["previous"],
        total: json["total"],
      );

  Map<String, dynamic> toJson() => {
        "href": href,
        "items": List<dynamic>.from(items.map((x) => x.toJson())),
        "limit": limit,
        "next": next,
        "offset": offset,
        "previous": previous,
        "total": total,
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
  dynamic primaryColor;
  dynamic public;
  String snapshotId;
  Tracks tracks;
  ItemType type;
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
    required this.primaryColor,
    required this.public,
    required this.snapshotId,
    required this.tracks,
    required this.type,
    required this.uri,
  });

  factory PlaylistItem.fromRawJson(String str) =>
      PlaylistItem.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory PlaylistItem.fromJson(Map<String, dynamic> json) => PlaylistItem(
        collaborative: json["collaborative"],
        description: json["description"],
        externalUrls: ExternalUrls.fromJson(json["external_urls"]),
        href: json["href"],
        id: json["id"],
        images: List<Image>.from(json["images"].map((x) => Image.fromJson(x))),
        name: json["name"],
        owner: Owner.fromJson(json["owner"]),
        primaryColor: json["primary_color"],
        public: json["public"],
        snapshotId: json["snapshot_id"],
        tracks: Tracks.fromJson(json["tracks"]),
        type: itemTypeValues.map[json["type"]]!,
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
        "primary_color": primaryColor,
        "public": public,
        "snapshot_id": snapshotId,
        "tracks": tracks.toJson(),
        "type": itemTypeValues.reverse[type],
        "uri": uri,
      };
}

class ExternalUrls {
  String spotify;

  ExternalUrls({
    required this.spotify,
  });

  factory ExternalUrls.fromRawJson(String str) =>
      ExternalUrls.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory ExternalUrls.fromJson(Map<String, dynamic> json) => ExternalUrls(
        spotify: json["spotify"],
      );

  Map<String, dynamic> toJson() => {
        "spotify": spotify,
      };
}

class Image {
  dynamic height;
  String url;
  dynamic width;

  Image({
    required this.height,
    required this.url,
    required this.width,
  });

  factory Image.fromRawJson(String str) => Image.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory Image.fromJson(Map<String, dynamic> json) => Image(
        height: json["height"],
        url: json["url"],
        width: json["width"],
      );

  Map<String, dynamic> toJson() => {
        "height": height,
        "url": url,
        "width": width,
      };
}

class Owner {
  DisplayName displayName;
  ExternalUrls externalUrls;
  String href;
  Id id;
  OwnerType type;
  Uri uri;

  Owner({
    required this.displayName,
    required this.externalUrls,
    required this.href,
    required this.id,
    required this.type,
    required this.uri,
  });

  factory Owner.fromRawJson(String str) => Owner.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory Owner.fromJson(Map<String, dynamic> json) => Owner(
        displayName: displayNameValues.map[json["display_name"]]!,
        externalUrls: ExternalUrls.fromJson(json["external_urls"]),
        href: json["href"],
        id: idValues.map[json["id"]]!,
        type: ownerTypeValues.map[json["type"]]!,
        uri: uriValues.map[json["uri"]]!,
      );

  Map<String, dynamic> toJson() => {
        "display_name": displayNameValues.reverse[displayName],
        "external_urls": externalUrls.toJson(),
        "href": href,
        "id": idValues.reverse[id],
        "type": ownerTypeValues.reverse[type],
        "uri": uriValues.reverse[uri],
      };
}

enum DisplayName { SPOTIFY }

final displayNameValues = EnumValues({"Spotify": DisplayName.SPOTIFY});

enum Id { SPOTIFY }

final idValues = EnumValues({"spotify": Id.SPOTIFY});

enum OwnerType { USER }

final ownerTypeValues = EnumValues({"user": OwnerType.USER});

enum Uri { SPOTIFY_USER_SPOTIFY }

final uriValues =
    EnumValues({"spotify:user:spotify": Uri.SPOTIFY_USER_SPOTIFY});

class Tracks {
  String href;
  int total;

  Tracks({
    required this.href,
    required this.total,
  });

  factory Tracks.fromRawJson(String str) => Tracks.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory Tracks.fromJson(Map<String, dynamic> json) => Tracks(
        href: json["href"],
        total: json["total"],
      );

  Map<String, dynamic> toJson() => {
        "href": href,
        "total": total,
      };
}

enum ItemType { PLAYLIST }

final itemTypeValues = EnumValues({"playlist": ItemType.PLAYLIST});

class EnumValues<T> {
  Map<String, T> map;
  late Map<T, String> reverseMap;

  EnumValues(this.map);

  Map<T, String> get reverse {
    reverseMap = map.map((k, v) => MapEntry(v, k));
    return reverseMap;
  }
}
