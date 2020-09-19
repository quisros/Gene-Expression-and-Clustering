source('qbwRModule.R')

mrna.data = getMrnaData()
dim(mrna.data)
head(mrna.data)

patient.data = getPatientData()
dim(patient.data)
head(patient.data)

sd(mrna.data[1,])

all.sds = apply(mrna.data,1,sd)
head(all.sds)
sorted.sds = sort(all.sds, decreasing = T)
head(sorted.sds)

print(sorted.sds[2000])

sorted.order = order(all.sds, decreasing=T)
sorted.matrix = mrna.data[sorted.order,]

m = matrix(c(1,2,3,4,5,6), nrow=2)
m
pheatmap::pheatmap(m)

m = matrix(seq(1,25),nrow=5)
m
pheatmap::pheatmap(m)

pheatmap::pheatmap(sorted.matrix[1:10,],scale='row')
ts = subset(patient.data, select='Tumor.subtype')
pheatmap::pheatmap(sorted.matrix[1:100,],annotation=ts,scale='row')

life.vector = rep(0, ncol(mrna.data))
life.vector[which(patient.data[,2]=='Alive')] = 1
head(life.vector)
cor(sorted.matrix[1,],life.vector)

all.cors = apply(sorted.matrix,1,function(x) cor(x,life.vector)^2)
head(all.cors)

all.raw.cors = apply(sorted.matrix,1,function(x) abs(cor(x,life.vector)))
head(all.raw.cors)
candidates = subset(all.raw.cors,all.raw.cors>=0.4)
print(candidates)

cor.matrix = sorted.matrix[order(all.cors,decreasing = T),]
surv = subset(patient.data, select='Death.status')
surv
pheatmap::pheatmap(cor.matrix[1:50,],annotation=surv, fontsize = 8, cellheight = 9, scale='row')
