import plotly
import plotly.graph_objs as go

def plotOnGraph() :
    limit = 500
    startingX = 2
    averageY = [1]
    averageX =[2]
    xValues = list()
    iterationValues = list()

    while startingX <= limit:
        x = startingX
        counter = 0
        xValues.insert(counter, startingX)
        while x != 1:
            counter += 1
            if x % 2 != 0:
                x = (x * 3) + 1
            else:
                x = x / 2
        #print("The #" + str(startingX) + " takes " + str(counter) + " times.")
        iterationValues.insert(0, counter)
        startingX += 1
    iterationTotal = int(len(iterationValues) + 1)
    iterationAverage = float(sum(iterationValues) / len(iterationValues))
    #print(iterationAverage)

    trace1 = go.Scatter(
        x = xValues,
        y = iterationValues,
        name = "Iterations",
    )
    data = [trace1]
    # Edit the layout
    layout = dict(title = 'Collatz Pattern',
                  xaxis = dict(title = 'Numerical Value'),
                  yaxis = dict(title = 'Iterations Needed'),
                  )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='styled-line.html')

plotOnGraph()