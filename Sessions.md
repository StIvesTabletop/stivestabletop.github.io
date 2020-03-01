---
title: RPG Sessions
---

{%- assign sessions = site.data.sessions.sessions -%}

<ul class="postlist">
    {% for session in sessions %}
        <li>
            <p><a href="{{ session.url }}">{{ session.title }}</a><br>
            <span class="postexcerpt">{{ session.date }}</span></p>
        </li>
    {% endfor %}
</ul>
