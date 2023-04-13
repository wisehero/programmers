def solution(genres, plays):
    answer = []
    genres_dict = {}
    plays_dict = {}

    for genre in genres:
        genres_dict[genre] = 0
    for i, v in enumerate(plays):
        plays_dict[i] = (genres[i], v)

    for i, v in plays_dict.values():
        genres_dict[i] += v

    best_two_songs = {}
    for g in dict(sorted(genres_dict.items(), key=lambda x: -x[1])).keys():
        best_two_songs[g] = []

    for serial, genre_play in sorted(plays_dict.items(), key=lambda x: (x[1], x[0]), reverse=True):
        if len(best_two_songs[genre_play[0]]) < 2:
            best_two_songs[genre_play[0]].append(serial)

    for key in best_two_songs.keys():
        answer += best_two_songs[key]

    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 800, 800, 2500])
