walking_speed = float(input("Enter your average walking speed in km/h: "))
extra_time_walking = float(input("Enter the amount of time you need, in minutes, "
                                "for additional activities when walking (e.g. tying your shoelaces or "
                                "grabbing an umbrella): "))

driving_speed = float(input("Enter your average driving speed in km/h: "))
extra_time_driving = float(input("Enter the amount of time you need, in minutes, "
                                 "for additional activities when driving (e.g. parking and "
                                 "walking from the parking spot to the destination): "))

cycling_speed = float(input("Enter your average cycling speed in km/h: "))
extra_time_cycling = float(input("Enter the amount of time you need, in minutes, "
                                 "for additional activities when cycling (e.g. getting "
                                 "your bicycle out of the shed and parking it): "))

distance = float(input("Enter the distance to your destination in kilometres: "))

walking_time_hours = int(distance//walking_speed)
walking_time_minutes = int(((distance % walking_speed)/walking_speed)*60 + int(extra_time_walking))
print("It will take you " + str(walking_time_hours) + " hour(s) and "
      + str(walking_time_minutes) + " minutes to get to your destination when walking,")

driving_time_hours = int(distance//driving_speed)
driving_time_minutes = int(((distance % driving_speed)/driving_speed)*60 + int(extra_time_driving))
print(str(driving_time_hours) + " hour(s) and "
      + str(driving_time_minutes) + " minutes when driving,")

cycling_time_hours = int(distance//cycling_speed)
cycling_time_minutes = int(((distance % cycling_speed)/cycling_speed)*60 + int(extra_time_cycling))
print("and " + str(cycling_time_hours) + " hour(s) and "
      + str(cycling_time_minutes) + " minutes when cycling.")