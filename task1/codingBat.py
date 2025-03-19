#WARMUP 1

#1
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#2
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
      return True
    else:
      return False

#3
def sum_double(a, b):
  if(a != b):
    return a+b
  else:
    return 2*(a+b)

#4
def diff21(n):
  if(n<21):
    return 21-n
  else:
    return 2*abs(21-n)
  
#5
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#6
def makes10(a, b):
  if(a == 10 or b==10):
    return True
  elif(a+b == 10):
    return True
  else:
    return False
  
#7
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#8
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  
#9
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

#10
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

#11
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]

#12
def front3(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 

#WARMUP 2

#1
def string_times(str, n):
  return n * str

#2
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

#3
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#4
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

#5
def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

#6
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1

  return count

#7
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

#8
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#9
def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  

  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

#STRING 1

#1
def hello_name(name):
  return "Hello " + name + "!"

#2
def make_abba(a, b):
  return a + b + b + a

#3
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

#4
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#5
def extra_end(str):
  return 3 * (str[-2] + str[-1])

#6
def first_two(str):
  if(str<2):
    return str
  else:
    return str[:2]

#7
def first_half(str):
  mid = len(str) / 2
  return str[:mid]

#8
def without_end(str):
  return str[1:-1]

#9
def combo_string(a, b):
  if(len(a)>len(b)):
    return b + a + b
  else:
    return a + b + a
  
#10
def non_start(a, b):
  return a[1:]+ b[1:]

#11
def left2(str):
  if(len(str) > 2):
    return str[2:] + str[:2]
  else:
    return str
  
#LIST-1
  
#1
def first_last6(nums):
    if(nums[0] == 6 or nums[-1] == 6):
      return True
    return False

#2
def make_pi():
  return [3, 1, 4]

#3
def common_end(a, b):
  if(a[0] == b[0] or a[-1] == b[-1]):
    return True
  return False

#4
def sum3(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

#5
def rotate_left3(nums):
  temp = nums[0]
  temp1 = nums[2]
  nums[0] = nums[1]
  nums[1] = temp1
  nums[2] = temp
  return nums

#6
def reverse3(nums):
  a = [0] * 3
  for i in range(2, -1, -1):
    a[2-i] = nums[i]
  return a

#7
def max_end3(nums):
  max_el = nums[0]
  if(nums[-1] > max_el):
    max_el = nums[-1]
  
  for i in range(0, len(nums)):
    nums[i] = max_el
  
  return nums

#8
def sum2(nums):
  if(len(nums)<2):
    return sum(nums)
  else:
    return nums[0] + nums[1]

#9
def middle_way(a, b):
  nums = [0] * 2 
  nums[0] = a[1]
  nums[1] = b[1]
  return nums

#10  
def make_ends(nums):
  numbs = [0] * 2
  numbs[0] = nums[0]
  numbs[1] = nums[-1]
  return numbs

#11
def has23(a):
  if(a[0] == 2 or a[0] == 3 or a[1] == 2 or a[1] == 3):
    return True
  return False


#LOGIC-1

#1
def cigar_party(cigars, is_weekend):
  if(cigars >= 40 and cigars <= 60 and is_weekend == False):
    return True
  elif(cigars >= 40 and is_weekend == True):
    return True
  else:
    return False

#2
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0  
    if you >= 8 or date >= 8:
        return 2
    return 1 

#3
def squirrel_play(temp, is_summer):
  if(temp >= 60 and temp <= 90 and is_summer == False):
    return True
  elif(temp >= 60 and temp <= 100 and is_summer == True):
    return True
  else:
    return False
  
#4
def caught_speeding(speed, is_birthday):
  if is_birthday:
      speed -= 5 
  
  if speed <= 60:
      return 0
  elif 61 <= speed <= 80:
      return 1
  else:
      return 2

#5
def sorta_sum(a, b):
  def sum(d, e):
    return d + e
  if(sum(a,b) >= 10 and sum(a,b) <= 19):
    return 20
  return sum(a, b)

#6
def alarm_clock(day, vacation):
  if vacation:
      return "10:00" if 1 <= day <= 5 else "off"
  else:
      return "7:00" if 1 <= day <= 5 else "10:00"  


#7
def love6(a, b):
  if a == 6 or b == 6:
      return True
        
  return a + b == 6 or abs(a - b) == 6

#8
def in1to10(n, outside_mode):
  if outside_mode:
      return n <= 1 or n >= 10
        
  return 1 <= n and n <= 10

#9
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8


#LOGIC-2

#1
def make_bricks(small, big, goal):
  if goal >= 5 * big:
      remainder = goal - (5 * big)
  else:
      remainder = goal % 5
      
  return small >= remainder

#2
def lone_sum(a, b, c):
  s = 0
  if a != b and a != c:
      s += a
          
  if b != a and b != c:
      s += b
                    
  if c != a and c != b:
      s += c
      
  return s

#3
def lucky_sum(a, b, c):
  if a == 13:
      return 0
      
  if b == 13:
      return a
              
  if c == 13:
      return a + b
                        
  return a + b + c

#4
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
  if 13 <= n and n <= 19 and n != 15 and n!= 16:
      return 0
          
  return n

#5
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
    
def round10(num):
  if num % 10 < 5:
      return num - (num % 10)
      
  return num + (10 - num % 10)

#6
def close_far(a, b, c):
  return (is_close(a, b) and is_far(a, b, c)) or (is_close(a, c) and is_far(a, c, b))
        
def is_close(a, b):
  return abs(a - b) <= 1
    
def is_far(a, b, c):
  return abs(a - c) >= 2 and abs(b - c) >= 2

#7
def make_chocolate(small, big, goal):
  if goal >= 5 * big:
      remainder = goal - 5 * big
  else:
      remainder = goal % 5
      
  if remainder <= small:
      return remainder
      
  return -1

#STRING 2

#1
def double_char(str):
  str2 = []
  for c in str:
      str2.append(2*c)
      
  return "".join(str2)

#2
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
      if str[i:i+2] == "hi":
          count += 1
          
  return count

#3
def cat_dog(str):
  cat = 0
  dog = 0
    
  for i in range(len(str) - 2):
      if str[i:i+3] == "cat":
          cat += 1
      elif str[i:i+3] == "dog":
          dog += 1
                                
  return cat == dog

#4
def count_code(str):
  count = 0
  for i in range(len(str)-3):
      if str[i:i+2] == "co" and str[i+3] == "e":
          count += 1
                  
  return count

#5
def end_other(a, b):
  a = a.lower()
  b = b.lower()
      
  return a.endswith(b) or b.endswith(a)

#6
def xyz_there(str):
  if str[:3] == "xyz":
      return True
                  
  for i in range(1, len(str) - 2):
      if str[i-1] != "." and str[i:i+3] == "xyz":
          return True
                                    
  return False

#LIST-2

#1
def count_evens(nums):
  count = 0
  for n in nums:
      if n % 2 == 0:
          count += 1
                  
  return count

#2
def big_diff(nums):
  minimum = nums[0]
  maximum = nums[0]
    
  for i in range(1,len(nums)):
      minimum = min(minimum, nums[i])
      maximum = max(maximum, nums[i])
                  
  return maximum - minimum

#3
def centered_average(nums):
  return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)

#4
def sum13(nums):
  s = 0
  i = 0
  while i < len(nums):
      if nums[i] == 13:
          i += 1
      else:
          s += nums[i]
          
      i += 1
      
  return s

#5
def sum67(nums):
  total = 0
  found6 = False
    
  for i in range(len(nums)):
      if nums[i] == 6:
          found6 = True
      if not found6:
          total += nums[i]
      if nums[i] == 7 and found6:
          found6 = False
          
  return total

#6
def has22(nums):
  for i in range(len(nums)-1):
      if nums[i] == 2 and nums[i+1] == 2:
          return True
                
  return False