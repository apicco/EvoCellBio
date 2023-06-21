
load('transform.mat')
W1files=dir('*.W1data.txt');
for i=1:length(W1files)
	sprintf(W1files(i).name)
	rawW1=load(W1files(i).name,'-ascii'); 
	
	%newW1=tforminv(warp,rawW1(:,2:3)); %old version for matlab2015
    newW1=warp.transformPointsInverse(rawW1(:,2:3));
	outputW1=[rawW1(:,1),newW1,rawW1(:,4:length(rawW1(1,:)))];
	save(W1files(i).name,'-ascii','outputW1')
	save(strcat(W1files(i).name(1:length(W1files(i).name)-4),'_original.txt'),'-ascii','rawW1')
end

exit
