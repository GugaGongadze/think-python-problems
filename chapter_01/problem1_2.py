# Q1. How many seconds are there in 42 minutes 42 seconds?
seconds_in_42_minutes_42_seconds = 42 * 60 + 42

# Q2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
miles_in_10k = 10 / 1.61

# Q3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
mile_in_seconds = seconds_in_42_minutes_42_seconds / miles_in_10k
print("Average pace: " + mile_in_seconds // 60 + " minutes and " + mile_in_seconds % 60 + " seconds.")