from utils import josn_to_dict









if __name__ == '__main__':
    subs_file = "subs.json"
    channel_list = josn_to_dict(subs_file)
    ch = channel_list[0]
    # for ch in channel_list:
    #     print(ch)
    print(ch)