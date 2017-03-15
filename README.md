# README

## XML formats for each individual component:
```xml
<xmldoc>
	<component value="rotor">
		<value="int (from 0 to 360)"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="temp">
		<value="int (from -100 to 100)"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="fanRPM">
		<value="int (from 0 to 100)"/>
	</component>
</xmldoc>
```

## General idea:
```
script rotate---\                                                      /---fan change direction
                 \                                                    /
script temp-------|--Mainscript-->LoadToQueue-->Logic-->LoadOnQueue--|----------------fan start
                 /                                                    \
script fanRPM---/                                                      \---------fan rpm change
```
