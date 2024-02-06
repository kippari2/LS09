--
-- WheelHydraulic
-- Specialization for wheel hydraulic animation
--
-- Modschmiede / LS-Modsource
-- @author  Manuel Leithner
-- @date  15/04/09
--

WheelHydraulic = {};

function WheelHydraulic.prerequisitesPresent(specializations)
    return true;
end;

function WheelHydraulic:load(xmlFile)

	self.drivingHydraulicCount = Utils.getNoNil(getXMLInt(xmlFile, "vehicle.drivingHydraulic#count"), 0);	
	if self.drivingHydraulicCount == 0 then
        print("Error: No drivingHydraulics specified - Count: 0", configFile);
    end;
	
	self.drivingHydraulic = {};	
	for i=1, self.drivingHydraulicCount do
		local hydraulicName = string.format("vehicle.drivingHydraulic.drivingHydraulic%d", i);
		
		self.drivingHydraulic[i] = {};		
		self.drivingHydraulic[i].node = Utils.indexToObject(self.components, getXMLString(xmlFile, hydraulicName .. "#hydraulic"));
		self.drivingHydraulic[i].punch = Utils.indexToObject(self.components, getXMLString(xmlFile, hydraulicName .. "#hydraulicPunch"));
		self.drivingHydraulic[i].translationPunch = Utils.indexToObject(self.components, getXMLString(xmlFile, hydraulicName .. "#hydraulicPunchFixPoint"));
		self.drivingHydraulic[i].fenderFixPoint = Utils.indexToObject(self.components, getXMLString(xmlFile, hydraulicName .. "#fenderFixPoint"));
		local ax, ay, az = getWorldTranslation(self.drivingHydraulic[i].punch);
		local bx, by, bz = getWorldTranslation(self.drivingHydraulic[i].translationPunch);		
		self.drivingHydraulic[i].punchDistance = Utils.vector3Length(ax-bx, ay-by, az-bz);	
	end;
end;

function WheelHydraulic:delete()
end;

function WheelHydraulic:mouseEvent(posX, posY, isDown, isUp, button)
end;

function WheelHydraulic:keyEvent(unicode, sym, modifier, isDown)
end;

function WheelHydraulic:update(dt)

	for i=1, table.getn(self.drivingHydraulic) do
		local ax, ay, az = getWorldTranslation(self.drivingHydraulic[i].node);
		local bx, by, bz = getWorldTranslation(self.drivingHydraulic[i].fenderFixPoint);
		local x, y, z = worldDirectionToLocal(getParent(self.drivingHydraulic[i].node), bx-ax, by-ay, bz-az);
		
		setDirection(self.drivingHydraulic[i].node, x, y, z, 0, 1, 0);
		if self.drivingHydraulic[i].punch ~= nil then
			local distance = Utils.vector3Length(ax-bx, ay-by, az-bz);
			setTranslation(self.drivingHydraulic[i].punch, 0, 0, distance-self.drivingHydraulic[i].punchDistance);
		end;	
	end;
		
end;

function WheelHydraulic:draw()
end;
