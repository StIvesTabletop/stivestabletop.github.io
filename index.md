---
title: Welcome
---

{% assign d = site.data.SessionInformation.NextSessionDate | date: "%-d" %}

# What is St. Ives Tabletop?

St Ives Tabletop is a fortnightly tabletop gaming group for the area around St. Ives, Cambridgeshire.

We cover:
* Tabletop role-playing games (RPGs), of which we have a good amount of experience running; and
* Board games, of which we have hundreds between us!

# Next session

In light of the recent easing of restrictions related to COVID-19 (aka coronavirus), we have restarted in-person St Ives Tabletop sessions as of 25th August 2021, and continuing fortnightly on Wednesday evenings.
Join the [Discord][Discord] server if you have any questions!


The next session will be:  
*{%- case d %}
	{%- when "1" or "21" or "31" %}{{ d }}st
	{%- when "2" or "22" %}{{ d }}nd
	{%- when "3" or "23" %}{{ d }}rd
	{%- else %}{{ d }}th
{%- endcase %} {{ site.data.SessionInformation.NextSessionDate | date: "%B %Y" }} @ {{ site.data.SessionInformation.SessionStart | date: "%l:%M%P" }} until {{ site.data.SessionInformation.SessionEnd | date: "%l:%M%P"}}*

See the [calendar](/Calendar.html) for the following sessions.

![Poster](/images/{{ site.data.SessionInformation.NextSessionDate | date: "%Y_%m_%d"}}_Poster.png "Next Session: {% case d %}
	{%- when "1" or "21" or "31" %}{{ d }}st
	{%- when "2" or "22" %}{{ d }}nd
	{%- when "3" or "23" %}{{ d }}rd
	{%- else %}{{ d }}th
{%- endcase %} {{ site.data.SessionInformation.NextSessionDate | date: "%B %Y" }}"){:class="img_poster"}

[Discord]: https://discord.gg/bScV82f
