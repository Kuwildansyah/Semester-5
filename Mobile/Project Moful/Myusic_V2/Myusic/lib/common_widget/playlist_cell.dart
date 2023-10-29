import 'package:flutter/material.dart';
import 'package:music_player/model/spotify_popular_playlist.dart' hide Image;

import '../common/color_extension.dart';

class PlaylistCell extends StatelessWidget {
  final PlaylistItem mObj;
  const PlaylistCell({super.key, required this.mObj});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 110,
      margin: const EdgeInsets.symmetric(horizontal: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          ClipRRect(
            borderRadius: BorderRadius.circular(9),
            child: Image.network(
              mObj.images[0].url,
              width: double.maxFinite,
              height: 110,
              fit: BoxFit.cover,
            ),
          ),
          const SizedBox(
            height: 15,
          ),
          Text(
            mObj.name,
            maxLines: 1,
            style: TextStyle(
                color: TColor.primaryText60,
                fontSize: 13,
                fontWeight: FontWeight.w700),
          ),
          Text(
            mObj.description,
            maxLines: 1,
            style: TextStyle(
                overflow: TextOverflow.ellipsis,
                color: TColor.secondaryText,
                fontSize: 10,
                fontWeight: FontWeight.w700),
          )
        ],
      ),
    );
  }
}
