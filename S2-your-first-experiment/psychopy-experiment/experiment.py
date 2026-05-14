#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Spatial Stroop Task (Simon effect)
-------------------------------------------------------------
In this experiment, participants will respond to the DIRECTION
of arrows ignoring their LOCATION. On 50% of trials, the arrow 
direction and location will match (CONGRUENT conditions), in the
remaining 50% they will be INCONGRUENT. 

The script requires: 
- Trial list .csv file (trial_list_1.csv)
- Folder with the stimulus images (stim/arrow_left.png and stim/arrow_right.png)

This material was created by Ana F Palenciano, Chiara Avancini, Giada Viviani
and Elisa Tentori, and is part of the SheCodesPsy 2026 Workshop. Visit our website 
(https://shecodespsy.github.io/) or our repository 
(https://github.com/shecodespsy/SheCodesPsy-2026) gto know more about our project 
and download all the materials. 

"""

from psychopy import visual, core, event, gui, data
import random
import pandas as pd
import os

# =============================================================================
# GET SUBJECT DEMOGRAPHIC INFO
# =============================================================================

# Dictionary with participant info:
info = {
    'Participant ID': '',
    'Age': '',
    'Gender': ['Prefer not to say', 'Female', 'Male', 'Non-binary'],
    'Handedness': ['Right', 'Left', 'Ambidextrous']
}

# Open interface to get the info:
dialog = gui.DlgFromDict(info, title='Spatial Stroop Task', order=[
    'Participant ID', 'Age', 'Gender', 'Handedness'
])

if not dialog.OK:
    core.quit()  # User pressed Cancel

# =============================================================================
# SETUP (AND CREATE, IF NEEDED) A DIRECTORY TO STORE THE RESULTS
# =============================================================================

if not os.path.exists('results'): # Create results folder if it doesn't exist
    os.makedirs('results')  

# =============================================================================
# SETUP: WINDOW, CLOCK, KEYBOARD, and GENERAL TASK VARIABLES
# =============================================================================

# Create a clock to measure time along your experiment
clock = core.Clock()

# Set up the monitor:  monitor ID, resolution, sampling rate, etc.
win = visual.Window(size=[1000, 600], color='white', units='pix', fullscr = False)

# Set up the keyboard: clean past events and decide keys allowed 
event.clearEvents()
keys_allowed = ['s','l','space','escape']

# Define basic task information, such as:
N_BLOCKS = 2
N_TRIALS = 20
# Define the position of our stimuli depending on the block condition
POSITION_CENTRAL = {
    'left':  [-75, 0],
    'right': [+75, 0]
}
POSITION_PERIPHERAL = {
    'left':  [-300, 0],
    'right': [+300, 0]
}
# =============================================================================
# SET UP THE TRIAL STIMULI
# =============================================================================
# We can create two types of stimuli

# A) Stimuli fixed since the beginning. E.g., the fixation cross 
fixation = visual.TextStim(win, text='+',color='black',height=40)

# B) Stimuli that change trial-by-trial: 
# The arrow (on each trial, we change the image and its location)
arrow = visual.ImageStim(win, size=[70, 50])
# The feedback we give the participants (updated after the response)
feedback = visual.TextStim(win, text='',color='',height=30)

# =============================================================================
# SHOW THE EXPERIMENT INSTRUCTIONS // WE CAN SKIP THIS 
# =============================================================================
# Remember: three steps to display an stimuli...
# 1) Set up / update the stimuli parameters (text, image, size, location...)
instructions = visual.TextStim(win,
    text=(
        "In this experiment, your task will be to respond \n to the DIRECTION of the arrows:\n\n"
        "   Arrow pointing left  →  press  F  (left index finger)\n"
        "   Arrow pointing right  →  press  J  (right index finger)\n\n"
        "The arrows will appear either on the left or the \n right side of the screen.\n\n"
        "Please, ignore the location of the arrows: \n only their DIRECTION matters.\n\n"
        "Press SPACE to begin."
    ),
    color='black',
    height=18,
    wrapWidth=win.size[0]*0.6
)
# 2) DRAW (or PREPARE) the stimuli...
instructions.draw()
# 3) FLIP the window to SHOW the stimuli!
win.flip()

# This is also a good moment to remember how we control the KEYBOARD:
event.waitKeys(keyList=['space'])
# Python will stop here and wait FOREVER... until you press space

# =============================================================================
# BLOCK LOOP
# =============================================================================

for block in range(N_BLOCKS):     # Repeat this for every block...
    print('block no. ' + str(block + 1) + ' starting now...')
    block_instr = visual.TextStim(win,color='black',height=28)
    block_instr.text = 'Block ' + str(block+1) + '. Press SPACEBAR to start'
    block_instr.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    # =============================================================================
    # Load the block trial list .csv file) and set up the block output file 
    # =============================================================================

    # This file was created in the previous step, and contains these columns:
    #   trial_number     : from 1 to 20  
    #   direction        : 'left' or 'right'
    #   position         : 'left' or 'right'
    #   congruency       : 'congruent' or 'incongruent'
    #   correct_response : 'l' or 's'
    trial_list = pd.read_csv('trial_list_' + str(block+1) +'.csv')
    
    # Set up the results VARIABLE (dictionary) and the FILE where it'll be stored:
    results = [] 
    output_name = 'results/sub' + str(info['Participant ID']) + '_block' + str(block+1) + 'results.csv'

    # =============================================================================
    # TRIAL LOOP
    # =============================================================================
    for trial in range(5):#range(N_TRIALS): # Repeat this for every trial...
        print('trial no. ' + str(trial+1) + ' starting now...')
        
        # 1. Fixation cross
        fixation.draw() # Prepare...
        win.flip()      # Show!
        core.wait(1)  # Leave it on screen for 500ms
        # core.wait(random.uniform(0.5,1))
        
        # 2. Stimulus
        # Set up the current trial stimulus image and the position
        arrow.image = 'stim/arrow_' + trial_list['direction'][trial] + '.png'
        if trial_list['block_type'][trial] == 'central':
            arrow.pos   = POSITION_CENTRAL[trial_list['position'][trial]] 
        elif trial_list['block_type'][trial] == 'peripheral':
            arrow.pos   = POSITION_PERIPHERAL[trial_list['position'][trial]]
        fixation.draw()  # Prepare (fixation cross)... 
        arrow.draw()     # Prepare (arrow stimulus)... 
        win.flip()       # Show!

        # 3. Get the participant response 
        # Restart the clock with the stimulus (presetation = 0ms) 
        event.clearEvents()
        clock.reset()       
        # Collect key presses (from target keys) for 2 secons     
        keys = event.waitKeys(
            maxWait=1.0,
            keyList= keys_allowed,
            timeStamped=clock # RT is computed using our clock as reference! 
        )
        
        # 4. Proccess the responses to get: key pressed, RT, accuracy
        if keys: 
            # If there a key has been pressed (there is a True in keys)...
            key, rt = keys[0] 
            correct = int(key == trial_list['correct_response'][trial])
        else:
            # Trials with no response
            key, rt, correct = 'none', None, 0  
        
        # 6. Show feedback
        if correct == 1: 
            feedback.text = 'correct!'
            feedback.color = 'green'
        elif correct == 0:
            feedback.text = 'wrong!'
            feedback.color = 'red'
        feedback.draw()
        win.flip()
        core.wait(0.5)
        
        # 7. Store everything...
        results.append({
            'participant': info['Participant ID'],
            'age':         info['Age'],
            'gender':      info['Gender'],
            'Handedness':  info['Handedness'],
            'trial':       trial + 1,
            'block':       block + 1,
            'condition':   trial_list['block_type'][trial],
            'direction':   trial_list['direction'][trial],
            'position':    trial_list['position'][trial],
            'congruency':  trial_list['congruency'][trial],
            'response':    key,
            'rt':          rt,
            'accuracy':    correct
        })
        # and start all over again! 

    # =============================================================================
    # SAVE OPUTPUT FILE 
    # =============================================================================

    # Store results to the output file:
    pd.DataFrame(results).to_csv(output_name, index=False)

# =============================================================================
# CLOSE EXPERIMENT
# =============================================================================

# Show a byebye message
farewell = visual.TextStim(win,
    text='All done! Thank you for participating.\n\nPress SPACE to exit.',
    color='black',
    height=28
)
farewell.draw()
win.flip()
event.waitKeys(keyList=['space'])

# Close the window so we can use the comptuer again!
win.close()