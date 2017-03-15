1. XML formats for each individual component:
<xmldoc>
	<component value="rotor">
		<value="int 0-360"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="temp">
		<value="int"/>
	</component>
</xmldoc>

<xmldoc>
	<component value="fanRPM">
		<value="int 0-100"/>
	</component>
</xmldoc>

2. General idea:
script rotate---\                                                      /--fan change direction
			     \                                                    /
script temp-------|--Mainscript-->LoadToQueue-->Logic-->LoadOnQueue--|----fan start
		         /                                                    \
script fanRPM---/                                                      \--fan rpm change

