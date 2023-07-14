def compress(chars):
    
    write_index = 0
    read_index = 0
    count = 0

    
    while read_index < len(chars):
        
        count += 1

        
        if read_index + 1 >= len(chars) or chars[read_index] != chars[read_index + 1]:
            chars[write_index] = chars[read_index]
            write_index += 1


            if count > 1:
                count_str = str(count)
                for char in count_str:
                    chars[write_index] = char
                    write_index += 1

        
            count = 0

        
        read_index += 1

    return write_index

# Driver code
chars = ["a", "a", "b", "b", "c", "c", "c"]
result = compress(chars)
print(result)
print(chars[:result])
