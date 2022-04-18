#to do: array with value for each knob, check if changed, print k_X like for b_x and delta
val_old=[None]*len(rotary_controller)
val_new=[None]*len(rotary_controller)
button_val_old=[None]*len(button_controller)
button_val_new=[None]*len(button_controller)

for i in range(0,len(rotary_controller)):
    val_old[i] = rotary_controller[i].value()
for i in range(0,len(button_controller)):
    button_val_old[i] = button_controller[i].value()
print("coucou")
while True:
    for i in range(0,len(rotary_controller)):
        val_new[i] = rotary_controller[i].value()

        if val_old[i] != val_new[i]:
            print('k_'+str(i),':', val_new[i]-val_old[i])
            val_old[i] = val_new[i]

    for i in range(0,len(button_controller)):
        button_val_new[i] = button_controller[i].value()
        if button_val_old[i] - button_val_new[i] == 1:
            print('b_'+str(i),'pressed')
        if button_val_old[i] - button_val_new[i] == -1:
            print('b_'+str(i),'released')
        button_val_old[i] = button_val_new[i]
    time.sleep_ms(10)
