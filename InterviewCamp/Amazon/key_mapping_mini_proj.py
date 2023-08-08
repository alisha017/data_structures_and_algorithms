import random
from typing import List


def get_combinations(access_keys_list: List[int], secret_keys_list: List[str], batch_size: int):
    result = []
    secret_keys_index = 0
    access_key_index = 0
    key_map_grid = {access_keys_list[i]: [0] * len(secret_keys_list) for i in range(len(access_keys_list))}

    while access_key_index < len(access_keys_list):
        current_access_key = access_keys_list[access_key_index]

        while secret_keys_index < len(secret_keys_list):

            if not key_map_grid[current_access_key][secret_keys_index]:
                current_batch = [current_access_key]
                current_batch.extend(secret_keys_list[secret_keys_index:secret_keys_index + batch_size])
                key_map_grid[current_access_key][secret_keys_index:secret_keys_index + batch_size] = [1] * batch_size
                result.append(current_batch)

            secret_keys_index += batch_size

        last_secret_keys_num = len(result[-1])-1
        if last_secret_keys_num < batch_size:
            access_keys_to_add = (batch_size - last_secret_keys_num) // last_secret_keys_num
        else:
            access_keys_to_add = 0
        print(f"last_secret_key_num:{last_secret_keys_num}, access_keys_to_add:{access_keys_to_add}")

        access_key_index += 1
        secret_keys_index = 0

        i = 0
        while i < access_keys_to_add and (access_key_index+i) < len(access_keys_list):
            to_add = access_keys_list[access_key_index + i]
            start_index = len(secret_keys_list)-last_secret_keys_num
            end_index = len(secret_keys_list)
            if key_map_grid[to_add][start_index:end_index] == [0]*last_secret_keys_num:
                result[-1].append(to_add)
                key_map_grid[to_add][start_index:end_index] = [1]*last_secret_keys_num
            i += 1

    return result


if __name__ == "__main__":
    access_key = list(range(1, 357))
    secret_key = [str(random.randint(1, 235)) for _ in range(235)]
    size = [4075]

    for s in size:
        answer = get_combinations(access_key, secret_key, s)
        # print(f"Batch size: {s}\t{answer}\n")
        print(f"Answer size: {len(answer)}")
        # print("*"*50)
