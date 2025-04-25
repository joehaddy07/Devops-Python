#DATA TYPE

#Integer: Represent whole numbers.
#my_integer = 42

#Float: Float numbers are specified with a decimal point.
#my_float = 4.2

#Strings: Are sequences of character data.
#my_strings = 't2.micro'

#Boolean: Can have either one of two values, True or False.
#is_on = True

def main():
    #strings (str)
    instance_type = 't2.micro'
    message = "my intance are of type: "

    #integer (int)
    number_of_instances = 5
    hours_running = 10

    print(f"{message} {instance_type}. I have {number_of_instances} of them and they have been running {hours_running} hours.")

    #boolean (bool)
    instances_running = True
    print(f"Are my intance running? {instances_running}.")
    print(f"my variable is of type: {type(instances_running)}.")



    #float
    ec2 = 10
    hours_running = 5.30
    total_pricing = ec2 + hours_running
    print(f'is the price: {total_pricing } usd.')




if __name__ == '__main__':
    main()