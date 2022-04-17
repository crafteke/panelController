#to do: array with value for each knob, check if changed, print k_X like for b_x and delta
val_old = rotary_controller[0].value()
while True:
    val_new = rotary_controller[0].value()

    if val_old != val_new:
        val_old = val_new
        print('k_0:', val_new-val_old)

    time.sleep_ms(10)
