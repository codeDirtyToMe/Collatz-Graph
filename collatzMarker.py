#!/usr/bin/python3.5
import plotly, logging
import plotly.graph_objs as go
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def plotOnGraph() :
    limit = 9000
    startingX = 2
    xValues = list()
    iterationValues = list()
    signChangesPos = list()
    signChangesNeg = list()

    while startingX <= limit:
        x = startingX
        counter = 0
        positiveSignChanges = int(0)
        negativeSignchanges = int(0)

        xValues.insert(counter, startingX) #List of values that been run.

        while x != 1:
            counter += 1
            if x % 2 != 0:
                x = (x * 3) + 1
                positiveSignChanges += 1
            else:
                x = x / 2
                negativeSignchanges -= 1

        iterationValues.insert(0, counter)
        signChangesPos.insert(0, positiveSignChanges) #Towards infinity
        signChangesNeg.insert(0, negativeSignchanges) #Towards 1
        startingX += 1

    logging.debug(iterationValues)
    logging.debug("Length of positive sign changes list: " + str(len(signChangesPos)))
    logging.debug(signChangesPos)
    logging.debug("Length of negative sign changes list: " + str(len(signChangesNeg)))
    logging.debug(signChangesNeg)

    trace1 = go.Scatter(
        x = xValues,
        y = iterationValues,
        name = "Iterations",
        mode = "markers"
    )

    trace2 = go.Scatter(
        x = xValues,
        y = signChangesPos,
        name = "+ Changes"
    )

    trace3 = go.Scatter(
        x = xValues,
        y = signChangesNeg,
        name = "- Changes"
    )
    data = [trace1]
    #data = [trace1, trace2, trace3]
    # Edit the layout
    layout = dict(title = 'Collatz Pattern',
                  xaxis = dict(title = 'Numerical Value'),
                  yaxis = dict(title = 'Iterations Needed'),
                  )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='styled-line.html')

plotOnGraph()
