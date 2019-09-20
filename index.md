---
title: Welcome
---

{% assign d = site.NextSessionDate | date: "%-d" %}

# What is St. Ives Tabletop?

We are starting a fortnightly tabletop group for the area around St. Ives, Cambridgeshire.

We aim to cover:
* tabletop RPGs (we have a good amount of experience running); and
* board games (we have hundreds between us!).

# Next session

*{%- case d %}
	{% when "1" or "21" or "31" %}{{ d }}st
	{% when "2" or "22" %}{{ d }}nd
	{% when "3" or "23" %}{{ d }}rd
	{% else %}{{ d }}th
{%- endcase %} {{ site.NextSessionDate | date: "%B %Y" }} @ {{ site.SessionStart | date: "%l:%M%P" }} until {{ site.SessionEnd | date: "%l:%M%P"}}*

See the [calendar](/Calendar.html) for the following sessions.

![Poster](/images/{{ site.NextSessionDate | date: "%Y_%m_%d"}}_Poster.png "Next Session: {% case d %}
	{% when "1" or "21" or "31" %}{{ d }}st
	{% when "2" or "22" %}{{ d }}nd
	{% when "3" or "23" %}{{ d }}rd
	{% else %}{{ d }}th
{%- endcase %} {{ site.NextSessionDate | date: "%B %Y" }}"){:class="img_poster"}
