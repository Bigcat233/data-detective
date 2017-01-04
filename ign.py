import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.charts import Donut
from bokeh.embed import components


def count_attribute(df, attribute):
	return df.get(attribute).value_counts().sort_index()


ign = pandas.read_csv('ign.csv')


# --- Basic ------------------------------------------------------------------------------------------------------------
def basic():
	# score_phrase
	score_phrase = count_attribute(ign, 'score_phrase')
	index = ['Masterpiece', 'Amazing', 'Great', 'Good', 'Okay', 'Bad', 'Awful', 'Painful', 'Unbearable', 'Disaster']
	score_phrase = score_phrase.reindex(index)
	plot_score_phrase = figure(width=800, x_range=list(score_phrase.keys().values))
	plot_score_phrase.vbar(x=list(score_phrase.keys().values), width=0.5, bottom=0, top=score_phrase.get_values(), color="#CAB2D6")

	# platform
	platform = count_attribute(ign, 'platform')
	platform = platform.nlargest(10)
	plot_platform = figure(width=800, x_range=list(platform.keys().values))
	plot_platform.vbar(x=list(platform.keys().values), width=0.5, bottom=0, top=platform.get_values(), color="#CAB2D6")

	# score
	score = count_attribute(ign, 'score')
	plot_score = figure()
	plot_score.vbar(x=list(score.keys().values), width=0.5, bottom=0, top=score.get_values(), color="#CAB2D6")

	# genre
	genre = count_attribute(ign, 'genre')
	genre = genre.nlargest(20)
	plot_genre = figure(width=1600, x_range=list(genre.keys().values))
	plot_genre.vbar(x=list(genre.keys().values), width=0.5, bottom=0, top=genre.get_values(), color="#CAB2D6")

	# editors_choice
	editors_choice = count_attribute(ign, 'editors_choice')
	plot_editors_choice = figure(x_range=list(editors_choice.keys().values))
	plot_editors_choice.vbar(x=list(editors_choice.keys().values), width=0.5, bottom=0, top=editors_choice.get_values())

	# release_year
	release_year = count_attribute(ign, 'release_year')
	plot_release_year = figure()
	plot_release_year.vbar(x=list(release_year.keys().values), width=0.5, bottom=0, top=release_year.get_values())

	# release_month
	release_month = count_attribute(ign, 'release_month')
	plot_release_month = figure()
	plot_release_month.vbar(x=list(release_month.keys().values), width=0.5, bottom=0, top=release_month.get_values())

	# release_day
	release_day = count_attribute(ign, 'release_day')
	plot_release_day = figure(width=1200)
	plot_release_day.vbar(x=list(release_day.keys().values), width=0.5, bottom=0, top=release_day.get_values())
	# --- Basic End --------------------------------------------------------------------------------------------------------


# --- 2010 - 2016 ---

def games_2010_2016():
	games = ign[(ign['release_year'] >= 2010) & (ign['release_year'] <= 2016)]
	print(games.shape[0], 'games from 2010 to 2016')

	# Platform
	platform = count_attribute(games, 'platform')
	platform = platform.nlargest(10)
	plot_platform = Donut(platform, plot_height=600, plot_width=600)

	# Genre
	genre = count_attribute(games, 'genre')
	genre = genre.nlargest(10)
	plot_genre = Donut(genre, plot_height=600, plot_width=600)

	editors_choice = count_attribute(games, 'editors_choice')
	plot_editors_choice = Donut(editors_choice, plot_height=600, plot_width=600)

	output_file("ign.html")
	grid = gridplot([
		[plot_platform, plot_genre, plot_editors_choice]
	])
	show(grid)

'''
Top 100 Games by Score
 - Platform
 - Genre
 - editors_choice
 '''
# top100 = ign.nlargest(1, 'score', keep='first')
# print(top100, top100.shape)

'''
Top 20 Games by Score

Top 10 Games by Score

Best Platform by average scores of games
Worst Platform by average scores of games
Percentage of good+ games of platforms
Percentage of bad+ games of platforms
Genres with Best Games
Genres with Worst Games

Summary
'''

games_2010_2016()
# --- 2010 - 2016 End ---


# output to static HTML file
# output_file("ign.html")
# grid = gridplot([
# 	[plot_score, None],
# 	[plot_platform, plot_score_phrase],
# 	[plot_genre],
# 	[plot_editors_choice, plot_release_year],
# 	[plot_release_day, plot_release_month]
# ])
# show(grid)
