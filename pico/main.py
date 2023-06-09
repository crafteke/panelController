#to do: array with value for each knob, check if changed, print k_X like for b_x and delta
val_old=[None]*len(rotary_controller)
val_new=[None]*len(rotary_controller)
button_val_old=[None]*len(button_controller)
button_val_new=[None]*len(button_controller)
button_time=[0]*len(button_controller)

adc_states=[0,0,0]
adc_time=[0,0,0]

for i in range(0,len(rotary_controller)):
    val_old[i] = rotary_controller[i].value()
for i in range(0,len(button_controller)):
    button_val_old[i] = button_controller[i].value()
while True:
    for i in range(0,len(rotary_controller)):
        val_new[i] = rotary_controller[i].value()
        if val_old[i] != val_new[i]:
            print(CONTROLLER_ID+'knob_'+str(i)+':'+str(val_new[i]-val_old[i]))
            val_old[i] = val_new[i]

    for i in range(0,len(button_controller)):
        button_val_new[i] = button_controller[i].value()
        if button_val_old[i] - button_val_new[i] == 1:
            button_time[i]=20
        if button_time[i] == 1:
            print(CONTROLLER_ID+'button_'+str(i)+':1')
        if button_val_old[i] - button_val_new[i] == -1:
            if button_time[i] == 1 or button_time[i] == 0:
                print(CONTROLLER_ID+'button_'+str(i)+':0')
            else:
                button_time[i]=1
        button_val_old[i] = button_val_new[i]
        if button_time[i] != 0:
            button_time[i] = button_time[i] - 1

    for i in range(0,3):
        adc_value=read_adc(i)
        if adc_value>0.5 and adc_time[i] < 30:
                adc_time[i]=adc_time[i]+1
        elif adc_time[i] > 0:
                adc_time[i]=adc_time[i]-1
        if adc_time[i]>=20:
            if adc_states[i]==0 and adc_value>1.4 and adc_value<1.8:
                print(CONTROLLER_ID+"plug_"+str(i)+':1')
                adc_states[i]=1
            elif  adc_states[i]==0 and adc_value>2.4 and adc_value<2.8:
                print(CONTROLLER_ID+"plug_"+str(i)+':2')
                adc_states[i]=2
        if adc_time[i] < 10:
            if adc_states[i]!=0:
                print(CONTROLLER_ID+"plug_"+str(i)+':0')
                adc_states[i]=0
    #time.sleep_ms(10)
