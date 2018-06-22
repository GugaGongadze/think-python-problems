# Q1.The volume of a sphere with radius r is (4/3)π(r^3). What is the volume of a sphere with radius 5?
import math
sphere_volume = (4/3) * math.pi * (5 ** 3)

# Q2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cover_price = 24.95
bookstore_price = cover_price * 60 / 100
first_copy_shipping = 3
additional_copy_shipping = 0.75
total_cost = bookstore_price * 60 + first_copy_shipping + 59 * additional_copy_shipping

# Q3.  If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
running_time_seconds = 2 * (8 * 60 + 15) + 3 * (7 * 60 + 12)
running_time_minutes = running_time_seconds // 60
# A1. I will be home at 7:30