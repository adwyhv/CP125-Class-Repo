def count_bright_spots(pixels):
    bright_spot_count = 0
    for i in range(len(pixels)):
         if i == 0 or i == len(pixels)-1:
             continue
         
         elif pixels[i] > pixels[i+1] and pixels[i] > pixels[i-1]:
              bright_spot_count +=1
    return bright_spot_count
              
         