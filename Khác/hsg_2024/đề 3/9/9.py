# Bài 9. Viết chương trình thực hiện công việc sau: (Sử dụng sắp xếp trộn)
# - Dữ liệu được nhập từ tệp văn bản Data.inp bao gồm hai dòng, mỗi dòng là một dãy các số nguyên đã được sắp xếp theo thứ tự tăng dần, các số cách nhau bởi dấu cách. Hai dãy này có thể không bằng nhau về kích thước.
# - Chương trình sẽ thực hiện trộn hai dãy trên và đưa kết quả dãy được trộn ra tệp Data.out theo một hàng ngang.


def merge_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


with open('Data.inp', 'r') as file:
    lines = file.readlines()

    arr1 = list(map(int, lines[0].strip().split()))
    arr2 = list(map(int, lines[1].strip().split()))


sx = merge_arrays(arr1,arr2)
with open('Data.out', 'w') as file:
    file.write(' '.join(map(str, sx)))
