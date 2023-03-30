#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 26, 2023, at 05:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'sample'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Work\\ETH Workshop\\workshop_work\\mysample\\sample_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "start_saccade" ---
text = visual.TextStim(win=win, name='text',
    text='You are going to see a Saccade task. \n\n:::: Press "Space" key to start ::::',
    font='Open Sans',
    pos=(0, 0), height=50.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_scade_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "cross_check" ---
corss_image = visual.ImageStim(
    win=win,
    name='corss_image', 
    image='D:/Work/ETH Workshop/workshop_work/eth_ws/stimuli/tcf05.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Saccade_Test" ---
# Run 'Begin Experiment' code from saccade_code
#image_smooth.pos=[-700,100]
#my_timer = core.Clock() 
#start_time = my_timer.getTime()
#print(start_time)
saccade_time_position=[]
sc_index=0

saccades_points=[]
saccades_points.append((-700,0))
saccades_points.append((700,0))
saccades_points.append((-700,0))
saccades_points.append((700,0))
saccades_points.append((-700,0))
saccades_points.append((700,0))
saccades_points.append((-700,0))
saccades_points.append((700,0))
sc_list_length = len(saccades_points)



saccade_image = visual.ImageStim(
    win=win,
    name='saccade_image', 
    image='stimuli/cat.png', mask=None, anchor='center',
    ori=0.0, pos=None, size=(220,150),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "start_smooth" ---
txt = visual.TextStim(win=win, name='txt',
    text='You are going to see a smooth pursuit task. \n\n:::: Press "Space" key to start ::::',
    font='Open Sans',
    pos=(0, 0), height=50.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_smoth_keybrd = keyboard.Keyboard()

# --- Initialize components for Routine "cross_check" ---
corss_image = visual.ImageStim(
    win=win,
    name='corss_image', 
    image='D:/Work/ETH Workshop/workshop_work/eth_ws/stimuli/tcf05.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "smooth_pursuit" ---
# Run 'Begin Experiment' code from code
#image_smooth.pos=[-700,100]

#generating list of points
first_line_points=[]
first_start_pos=-800
first_end_pos=800

#for(int i=0; i<9; i+=2)
for i in range(first_start_pos, first_end_pos, 1):
    pos=(i,100) #initialy it was 400
    first_line_points.append(pos)

#for i in range(first_start_pos, first_end_pos, 1):
#    pos=(i,100)
#    first_line_points.append(pos)

#for i in range(first_start_pos, first_end_pos, 1):
#    pos=(i,-400)
#    first_line_points.append(pos)
        
list_length = len(first_line_points)

image_smooth = visual.ImageStim(
    win=win,
    name='image_smooth', 
    image='stimuli/cat.png', mask=None, anchor='center',
    ori=0.0, pos=None, size=(220,150),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tr_smooth_key_smooth_resp_ = keyboard.Keyboard()

# --- Initialize components for Routine "start_circularM" ---
start_circleM = visual.TextStim(win=win, name='start_circleM',
    text='You are going to see a Circular Movement. \n \nKeep looking at the moving image.\n\n:::: Press "Space" key to start ::::',
    font='Open Sans',
    pos=(0, 0), height=50.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_circle_keyboard = keyboard.Keyboard()

# --- Initialize components for Routine "cross_check_circle" ---
cross_img_circle = visual.ImageStim(
    win=win,
    name='cross_img_circle', 
    image='D:/Work/ETH Workshop/workshop_work/eth_ws/stimuli/tcf05.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Circular_Movement" ---
# Run 'Begin Experiment' code from code_2
import math
import csv

def generate_circle_points(radius, interval):
    points = []
    for i in range(0, 360, interval):
        x = radius * math.cos(math.radians(i))
        y = radius * math.sin(math.radians(i))
        points.append((x, y))
    return points
    
points = generate_circle_points(radius=350, interval=1)

#get participant name
expInfo['participant']
csv_file_name =expInfo['participant']+'_circle_points.csv'
csv_file_path = 'circle_position/' + csv_file_name

#with open('stimuli_positions_data/circle_points.csv', 'w', newline='') as file:
# Writing the points to a CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    writer.writerows(points)
    
img_circle = visual.ImageStim(
    win=win,
    name='img_circle', 
    image='stimuli/Pan_Blue_Circle.png', mask=None, anchor='center',
    ori=0.0, pos=None, size=(60,60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tr_circ_resp_keyboard = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start_saccade" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_scade_key_resp.keys = []
start_scade_key_resp.rt = []
_start_scade_key_resp_allKeys = []
# keep track of which components have finished
start_saccadeComponents = [text, start_scade_key_resp]
for thisComponent in start_saccadeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_saccade" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *start_scade_key_resp* updates
    waitOnFlip = False
    if start_scade_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_scade_key_resp.frameNStart = frameN  # exact frame index
        start_scade_key_resp.tStart = t  # local t and not account for scr refresh
        start_scade_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_scade_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_scade_key_resp.started')
        start_scade_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_scade_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_scade_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_scade_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_scade_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _start_scade_key_resp_allKeys.extend(theseKeys)
        if len(_start_scade_key_resp_allKeys):
            start_scade_key_resp.keys = _start_scade_key_resp_allKeys[-1].name  # just the last key pressed
            start_scade_key_resp.rt = _start_scade_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_saccadeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_saccade" ---
for thisComponent in start_saccadeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_scade_key_resp.keys in ['', [], None]:  # No response was made
    start_scade_key_resp.keys = None
thisExp.addData('start_scade_key_resp.keys',start_scade_key_resp.keys)
if start_scade_key_resp.keys != None:  # we had a response
    thisExp.addData('start_scade_key_resp.rt', start_scade_key_resp.rt)
thisExp.nextEntry()
# the Routine "start_saccade" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cross_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
cross_checkComponents = [corss_image]
for thisComponent in cross_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "cross_check" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *corss_image* updates
    if corss_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        corss_image.frameNStart = frameN  # exact frame index
        corss_image.tStart = t  # local t and not account for scr refresh
        corss_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(corss_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'corss_image.started')
        corss_image.setAutoDraw(True)
    if corss_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > corss_image.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            corss_image.tStop = t  # not accounting for scr refresh
            corss_image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'corss_image.stopped')
            corss_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cross_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cross_check" ---
for thisComponent in cross_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Saccade_Test" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from saccade_code
    '''
    #image_smooth.pos=[-700,100]
    t = my_timer.getTime()
    #saccade_time.append(t)
    
    sc_list_length = len(saccades_points)
    sc_index=0
    img_circle.pos=saccades_points[sc_index]
    saccade_time_position.append((t,saccades_points[sc_index]))
    '''
    
    
    stim_start_time = core.Clock() 
    start_time_Sc=stim_start_time.getTime()
    
    
    time_data = []
    pos_data = []
    
     #stim_duration = 0.5 # duration of the stimulus in seconds
    
    if (sc_index<sc_list_length):
        saccade_image.pos=saccades_points[sc_index]
        sc_index=sc_index+1
        
    
    #while timer.getTime()<0:
    #while t < 0.5:
        #current_time = clock.getTime() - start_time
        #current_pos = saccade_image.pos
    #     t = stim_start_time.getTime()
        #time_data.append(current_time)
        #pos_data.append(current_pos)
    
    
    
    
    # keep track of which components have finished
    Saccade_TestComponents = [saccade_image]
    for thisComponent in Saccade_TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Saccade_Test" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from saccade_code
        '''
        t = my_timer.getTime()
        #saccade_time.append(t)
        print(t)
        if (sc_index<sc_list_length):
            saccade_image.pos=saccades_points[sc_index]
            saccade_time_position.append((t,saccades_points[sc_index]))
            sc_index=sc_index+1
            core.wait(0.5) # wait for 2 seconds
            
        else:
            continueRoutine = False
            
        '''
        
        
        # *saccade_image* updates
        if saccade_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            saccade_image.frameNStart = frameN  # exact frame index
            saccade_image.tStart = t  # local t and not account for scr refresh
            saccade_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(saccade_image, 'tStartRefresh')  # time at next scr refresh
            saccade_image.setAutoDraw(True)
        if saccade_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > saccade_image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                saccade_image.tStop = t  # not accounting for scr refresh
                saccade_image.frameNStop = frameN  # exact frame index
                saccade_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Saccade_TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Saccade_Test" ---
    for thisComponent in Saccade_TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from saccade_code
    '''
    expInfo['participant']
    csv_file_name =expInfo['participant']+'_saccade_time.csv'
    csv_file_path = 'saccade_position_time/' + csv_file_name
    
    #with open('stimuli_positions_data/circle_points.csv', 'w', newline='') as file:
    # Writing the points to a CSV file
    headers = ['time', 'img_position']
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['time', 'img_pos'])
        for tup in saccade_time_position:
            writer.writerow(tup)
    '''
    
    print("routine ended")
    elapsed_time = stim_start_time.getTime() - start_time_Sc
    
    # Print or store the elapsed time
    print("Elapsed time: %.2f seconds" % elapsed_time)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'


# --- Prepare to start Routine "start_smooth" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_smoth_keybrd.keys = []
start_smoth_keybrd.rt = []
_start_smoth_keybrd_allKeys = []
# keep track of which components have finished
start_smoothComponents = [txt, start_smoth_keybrd]
for thisComponent in start_smoothComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_smooth" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt* updates
    if txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt.frameNStart = frameN  # exact frame index
        txt.tStart = t  # local t and not account for scr refresh
        txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'txt.started')
        txt.setAutoDraw(True)
    
    # *start_smoth_keybrd* updates
    waitOnFlip = False
    if start_smoth_keybrd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_smoth_keybrd.frameNStart = frameN  # exact frame index
        start_smoth_keybrd.tStart = t  # local t and not account for scr refresh
        start_smoth_keybrd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_smoth_keybrd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_smoth_keybrd.started')
        start_smoth_keybrd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_smoth_keybrd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_smoth_keybrd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_smoth_keybrd.status == STARTED and not waitOnFlip:
        theseKeys = start_smoth_keybrd.getKeys(keyList=['space'], waitRelease=False)
        _start_smoth_keybrd_allKeys.extend(theseKeys)
        if len(_start_smoth_keybrd_allKeys):
            start_smoth_keybrd.keys = _start_smoth_keybrd_allKeys[-1].name  # just the last key pressed
            start_smoth_keybrd.rt = _start_smoth_keybrd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_smoothComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_smooth" ---
for thisComponent in start_smoothComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_smoth_keybrd.keys in ['', [], None]:  # No response was made
    start_smoth_keybrd.keys = None
thisExp.addData('start_smoth_keybrd.keys',start_smoth_keybrd.keys)
if start_smoth_keybrd.keys != None:  # we had a response
    thisExp.addData('start_smoth_keybrd.rt', start_smoth_keybrd.rt)
thisExp.nextEntry()
# the Routine "start_smooth" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cross_check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
cross_checkComponents = [corss_image]
for thisComponent in cross_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "cross_check" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *corss_image* updates
    if corss_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        corss_image.frameNStart = frameN  # exact frame index
        corss_image.tStart = t  # local t and not account for scr refresh
        corss_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(corss_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'corss_image.started')
        corss_image.setAutoDraw(True)
    if corss_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > corss_image.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            corss_image.tStop = t  # not accounting for scr refresh
            corss_image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'corss_image.stopped')
            corss_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cross_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cross_check" ---
for thisComponent in cross_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "smooth_pursuit" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code
#image_smooth.pos=[-700,100]
list_length = len(first_line_points)
index=0
image_smooth.pos=first_line_points[index]
tr_smooth_key_smooth_resp_.keys = []
tr_smooth_key_smooth_resp_.rt = []
_tr_smooth_key_smooth_resp__allKeys = []
# keep track of which components have finished
smooth_pursuitComponents = [image_smooth, tr_smooth_key_smooth_resp_]
for thisComponent in smooth_pursuitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "smooth_pursuit" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from code
    if(index<list_length):
        image_smooth.pos=first_line_points[index]
        index=index+1
        
    
    # *image_smooth* updates
    if image_smooth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_smooth.frameNStart = frameN  # exact frame index
        image_smooth.tStart = t  # local t and not account for scr refresh
        image_smooth.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_smooth, 'tStartRefresh')  # time at next scr refresh
        image_smooth.setAutoDraw(True)
    
    # *tr_smooth_key_smooth_resp_* updates
    waitOnFlip = False
    if tr_smooth_key_smooth_resp_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tr_smooth_key_smooth_resp_.frameNStart = frameN  # exact frame index
        tr_smooth_key_smooth_resp_.tStart = t  # local t and not account for scr refresh
        tr_smooth_key_smooth_resp_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tr_smooth_key_smooth_resp_, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tr_smooth_key_smooth_resp_.started')
        tr_smooth_key_smooth_resp_.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(tr_smooth_key_smooth_resp_.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(tr_smooth_key_smooth_resp_.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if tr_smooth_key_smooth_resp_.status == STARTED and not waitOnFlip:
        theseKeys = tr_smooth_key_smooth_resp_.getKeys(keyList=['space'], waitRelease=False)
        _tr_smooth_key_smooth_resp__allKeys.extend(theseKeys)
        if len(_tr_smooth_key_smooth_resp__allKeys):
            tr_smooth_key_smooth_resp_.keys = _tr_smooth_key_smooth_resp__allKeys[-1].name  # just the last key pressed
            tr_smooth_key_smooth_resp_.rt = _tr_smooth_key_smooth_resp__allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in smooth_pursuitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "smooth_pursuit" ---
for thisComponent in smooth_pursuitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if tr_smooth_key_smooth_resp_.keys in ['', [], None]:  # No response was made
    tr_smooth_key_smooth_resp_.keys = None
thisExp.addData('tr_smooth_key_smooth_resp_.keys',tr_smooth_key_smooth_resp_.keys)
if tr_smooth_key_smooth_resp_.keys != None:  # we had a response
    thisExp.addData('tr_smooth_key_smooth_resp_.rt', tr_smooth_key_smooth_resp_.rt)
thisExp.nextEntry()
# the Routine "smooth_pursuit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "start_circularM" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_circle_keyboard.keys = []
start_circle_keyboard.rt = []
_start_circle_keyboard_allKeys = []
# keep track of which components have finished
start_circularMComponents = [start_circleM, start_circle_keyboard]
for thisComponent in start_circularMComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_circularM" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_circleM* updates
    if start_circleM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_circleM.frameNStart = frameN  # exact frame index
        start_circleM.tStart = t  # local t and not account for scr refresh
        start_circleM.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_circleM, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_circleM.started')
        start_circleM.setAutoDraw(True)
    
    # *start_circle_keyboard* updates
    waitOnFlip = False
    if start_circle_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_circle_keyboard.frameNStart = frameN  # exact frame index
        start_circle_keyboard.tStart = t  # local t and not account for scr refresh
        start_circle_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_circle_keyboard, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_circle_keyboard.started')
        start_circle_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_circle_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_circle_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_circle_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = start_circle_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _start_circle_keyboard_allKeys.extend(theseKeys)
        if len(_start_circle_keyboard_allKeys):
            start_circle_keyboard.keys = _start_circle_keyboard_allKeys[-1].name  # just the last key pressed
            start_circle_keyboard.rt = _start_circle_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_circularMComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_circularM" ---
for thisComponent in start_circularMComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_circle_keyboard.keys in ['', [], None]:  # No response was made
    start_circle_keyboard.keys = None
thisExp.addData('start_circle_keyboard.keys',start_circle_keyboard.keys)
if start_circle_keyboard.keys != None:  # we had a response
    thisExp.addData('start_circle_keyboard.rt', start_circle_keyboard.rt)
thisExp.nextEntry()
# the Routine "start_circularM" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "cross_check_circle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
cross_check_circleComponents = [cross_img_circle]
for thisComponent in cross_check_circleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "cross_check_circle" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cross_img_circle* updates
    if cross_img_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross_img_circle.frameNStart = frameN  # exact frame index
        cross_img_circle.tStart = t  # local t and not account for scr refresh
        cross_img_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross_img_circle, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cross_img_circle.started')
        cross_img_circle.setAutoDraw(True)
    if cross_img_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross_img_circle.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            cross_img_circle.tStop = t  # not accounting for scr refresh
            cross_img_circle.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_img_circle.stopped')
            cross_img_circle.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cross_check_circleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "cross_check_circle" ---
for thisComponent in cross_check_circleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "Circular_Movement" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_2
# how many times do you want this cirlce to be repeated. Counter variable will count number of repitations.
number_of_repitations = 1
counter=0

list_length = len(points)
index=0
img_circle.pos=points[index]
tr_circ_resp_keyboard.keys = []
tr_circ_resp_keyboard.rt = []
_tr_circ_resp_keyboard_allKeys = []
# keep track of which components have finished
Circular_MovementComponents = [img_circle, tr_circ_resp_keyboard]
for thisComponent in Circular_MovementComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Circular_Movement" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from code_2
    
    if(index<list_length):
        img_circle.pos=points[index]
        index=index+1
    else:
        if(counter!=number_of_repitations):
            index=0
            counter=counter+1
        else:
            continueRoutine = False #ending rountine
    
    # *img_circle* updates
    if img_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_circle.frameNStart = frameN  # exact frame index
        img_circle.tStart = t  # local t and not account for scr refresh
        img_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_circle, 'tStartRefresh')  # time at next scr refresh
        img_circle.setAutoDraw(True)
    
    # *tr_circ_resp_keyboard* updates
    waitOnFlip = False
    if tr_circ_resp_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tr_circ_resp_keyboard.frameNStart = frameN  # exact frame index
        tr_circ_resp_keyboard.tStart = t  # local t and not account for scr refresh
        tr_circ_resp_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tr_circ_resp_keyboard, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tr_circ_resp_keyboard.started')
        tr_circ_resp_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(tr_circ_resp_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(tr_circ_resp_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if tr_circ_resp_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = tr_circ_resp_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _tr_circ_resp_keyboard_allKeys.extend(theseKeys)
        if len(_tr_circ_resp_keyboard_allKeys):
            tr_circ_resp_keyboard.keys = _tr_circ_resp_keyboard_allKeys[-1].name  # just the last key pressed
            tr_circ_resp_keyboard.rt = _tr_circ_resp_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Circular_MovementComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Circular_Movement" ---
for thisComponent in Circular_MovementComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if tr_circ_resp_keyboard.keys in ['', [], None]:  # No response was made
    tr_circ_resp_keyboard.keys = None
thisExp.addData('tr_circ_resp_keyboard.keys',tr_circ_resp_keyboard.keys)
if tr_circ_resp_keyboard.keys != None:  # we had a response
    thisExp.addData('tr_circ_resp_keyboard.rt', tr_circ_resp_keyboard.rt)
thisExp.nextEntry()
# the Routine "Circular_Movement" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from saccade_code
expInfo['participant']
csv_file_name =expInfo['participant']+'_saccade_time.csv'
csv_file_path = 'saccade_position_time/' + csv_file_name
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['time', 'img_pos'])
    for tup in saccade_time_position:
        writer.writerow(tup)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
